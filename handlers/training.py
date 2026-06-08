import json
from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

import database as db
from workouts import WORKOUTS, WORKOUT_CYCLE, week_to_phase, phase_start_index
from keyboards import exercise_kb, confirm_finish_kb, week_selection_kb

router = Router()


class TrainingStates(StatesGroup):
    waiting_for_week = State()
    waiting_for_result = State()


# Ключи в FSM-хранилище
SESSION_KEY = "session_id"
EXERCISE_INDEX_KEY = "exercise_idx"
WORKOUT_KEY_KEY = "workout_key"


def _format_exercise_card(ex: dict, idx: int, total: int, prev_result: list | None = None) -> str:
    input_hints = {
        "time": "⏱ Введи время каждого подхода через пробел (сек).\nПример: <code>10 11 9 10</code>",
        "reps": "🔢 Введи повторения каждого подхода через пробел.\nПример: <code>8 7 6 6</code>",
        "reps_weight": (
            "🏋️ Введи повторения×вес для каждого подхода.\n"
            "Пример: <code>6×+10 5×+10 5×+10 5×+10</code>\n"
            "Если без веса: <code>8 7 7 6</code>"
        ),
        "free": None,
    }

    lines = [
        f"<b>[{idx + 1}/{total}] {ex['name']}</b>",
        f"🎯 Цель: {ex['target']}  |  Подходов: {ex['sets']}",
    ]

    if prev_result and prev_result != ["пропущено"]:
        prev_str = "  |  ".join(prev_result)
        lines.append(f"🏆 Прошлый раз: <code>{prev_str}</code>")

    lines += ["", ex["description"], ""]

    if ex["input_type"] == "free":
        lines.append(f"✏️ {ex.get('prompt', 'Введи результат:')}")
    else:
        hint = input_hints.get(ex["input_type"], "✏️ Введи результат:")
        lines.append(hint)

    return "\n".join(lines)


async def _next_workout_key(user_id: int, week: int) -> tuple[str, int]:
    """Возвращает (ключ тренировки, новый next_workout_index)."""
    state = await db.get_user_state(user_id)
    if state is None:
        next_idx = phase_start_index(week_to_phase(week))
    else:
        next_idx = state["next_workout_index"]
    key = WORKOUT_CYCLE[next_idx % len(WORKOUT_CYCLE)]
    new_next_idx = (next_idx + 1) % len(WORKOUT_CYCLE)
    return key, new_next_idx


async def _send_exercise(message_or_cb, state: FSMContext, exercise_idx: int):
    if isinstance(message_or_cb, CallbackQuery):
        send = message_or_cb.message.answer
        user_id = message_or_cb.from_user.id
    else:
        send = message_or_cb.answer
        user_id = message_or_cb.from_user.id

    data = await state.get_data()
    workout_key = data[WORKOUT_KEY_KEY]
    workout = WORKOUTS[workout_key]
    exercises = workout["exercises"]
    total = len(exercises)

    if exercise_idx >= total:
        await _finish_workout(message_or_cb, state, completed=True)
        return

    ex = exercises[exercise_idx]
    prev_result = await db.get_last_exercise_result(user_id, ex["name"])
    text = _format_exercise_card(ex, exercise_idx, total, prev_result)
    await state.update_data({EXERCISE_INDEX_KEY: exercise_idx})
    await state.set_state(TrainingStates.waiting_for_result)
    await send(text, reply_markup=exercise_kb(), parse_mode="HTML")


async def _finish_workout(message_or_cb, state: FSMContext, completed: bool):
    if isinstance(message_or_cb, CallbackQuery):
        send = message_or_cb.message.answer
        user_id = message_or_cb.from_user.id
    else:
        send = message_or_cb.answer
        user_id = message_or_cb.from_user.id

    data = await state.get_data()
    session_id = data.get(SESSION_KEY)
    if session_id:
        await db.complete_session(session_id)

    await state.clear()

    if completed:
        await send("💪 <b>Тренировка завершена!</b> Отличная работа!\n\nДанные сохранены.", parse_mode="HTML")
    else:
        await send("🛑 Тренировка остановлена досрочно. Результаты сохранены.", parse_mode="HTML")


# --- Handlers ---

@router.message(F.text.in_({"🏋️ Начать тренировку", "/train"}))
async def cmd_train(message: Message, state: FSMContext):
    user_id = message.from_user.id
    user_state = await db.get_user_state(user_id)

    if user_state is None:
        await state.set_state(TrainingStates.waiting_for_week)
        await message.answer(
            "Привет! 👋\n\n<b>На какой неделе программы ты сейчас?</b>\n"
            "(1–12, выбери из кнопок ниже)",
            reply_markup=week_selection_kb(),
            parse_mode="HTML",
        )
        return

    await _start_workout(message, state, user_state["current_week"], user_id=message.from_user.id)


@router.callback_query(F.data.startswith("set_week:"), TrainingStates.waiting_for_week)
async def cb_set_week(callback: CallbackQuery, state: FSMContext):
    week = int(callback.data.split(":")[1])
    user_id = callback.from_user.id

    phase = week_to_phase(week)
    next_idx = phase_start_index(phase)
    await db.create_user_state(user_id, week, next_idx)

    await callback.message.edit_text(
        f"✅ Неделя <b>{week}</b> (Фаза {phase}) сохранена.", parse_mode="HTML"
    )
    await _start_workout(callback.message, state, week, user_id=user_id)


async def _start_workout(message, state: FSMContext, week: int, user_id: int):


    workout_key, new_next_idx = await _next_workout_key(user_id, week)
    await db.update_user_state(user_id, next_workout_index=new_next_idx)

    session_id = await db.create_session(user_id, workout_key)
    workout = WORKOUTS[workout_key]

    await state.update_data({
        SESSION_KEY: session_id,
        WORKOUT_KEY_KEY: workout_key,
        EXERCISE_INDEX_KEY: 0,
    })

    total = len(workout["exercises"])
    phase = workout_key.split("_")[0].replace("phase", "Фаза ")
    day = workout_key.split("_")[1].upper()
    await message.answer(
        f"🚀 <b>{workout['title']}</b>\n\n"
        f"Всего упражнений: <b>{total}</b>\nФаза {phase[-1]}, день {day}\n\n"
        "Начинаем!",
        parse_mode="HTML",
    )
    await _send_exercise(message, state, 0)


@router.message(TrainingStates.waiting_for_result)
async def handle_result(message: Message, state: FSMContext):
    data = await state.get_data()
    session_id = data[SESSION_KEY]
    exercise_idx = data[EXERCISE_INDEX_KEY]
    workout_key = data[WORKOUT_KEY_KEY]

    exercises = WORKOUTS[workout_key]["exercises"]
    ex = exercises[exercise_idx]

    sets_data = _parse_result(message.text, ex)
    await db.save_exercise_log(session_id, exercise_idx, ex["name"], sets_data)

    await _send_exercise(message, state, exercise_idx + 1)


def _parse_result(text: str, ex: dict) -> list:
    """Разбирает ввод пользователя в список строк (по одной на подход)."""
    parts = text.strip().split()
    if not parts:
        return [text.strip()]
    return parts


@router.callback_query(F.data == "skip_exercise", TrainingStates.waiting_for_result)
async def cb_skip(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    session_id = data[SESSION_KEY]
    exercise_idx = data[EXERCISE_INDEX_KEY]
    workout_key = data[WORKOUT_KEY_KEY]
    ex = WORKOUTS[workout_key]["exercises"][exercise_idx]

    await db.save_exercise_log(session_id, exercise_idx, ex["name"], ["пропущено"])
    await callback.answer("Упражнение пропущено")
    await _send_exercise(callback, state, exercise_idx + 1)


@router.callback_query(F.data == "finish_workout", TrainingStates.waiting_for_result)
async def cb_finish_prompt(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(
        "Завершить тренировку досрочно?",
        reply_markup=confirm_finish_kb(),
    )
    await callback.answer()


@router.callback_query(F.data == "confirm_finish")
async def cb_confirm_finish(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    await _finish_workout(callback, state, completed=False)


@router.callback_query(F.data == "continue_workout")
async def cb_continue(callback: CallbackQuery, state: FSMContext):
    await callback.message.delete()
    await callback.answer("Продолжаем! 💪")
