import json
from datetime import datetime
from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.filters import Command

import database as db
from workouts import WORKOUTS
from keyboards import stats_kb

router = Router()

WORKOUT_LABELS = {
    "phase1_A": "Ф1-А", "phase1_B": "Ф1-Б", "phase1_C": "Ф1-В",
    "phase2_A": "Ф2-А", "phase2_B": "Ф2-Б", "phase2_C": "Ф2-В",
    "phase3_A": "Ф3-А", "phase3_B": "Ф3-Б", "phase3_C": "Ф3-В",
}


class StatsStates(StatesGroup):
    waiting_for_exercise_name = State()


def _fmt_date(iso: str) -> str:
    try:
        dt = datetime.fromisoformat(iso)
        return dt.strftime("%d.%m.%Y")
    except Exception:
        return iso[:10]


@router.message(F.text.in_({"📅 История", "/history"}))
async def cmd_history(message: Message):
    user_id = message.from_user.id
    sessions = await db.get_last_sessions(user_id, limit=10)

    if not sessions:
        await message.answer("Тренировок пока нет. Напиши /train чтобы начать!")
        return

    lines = ["<b>📅 Последние тренировки:</b>\n"]
    for s in sessions:
        label = WORKOUT_LABELS.get(s["workout_key"], s["workout_key"])
        date = _fmt_date(s["started_at"])
        status = "✅" if s["completed_at"] else "⏸"
        lines.append(f"{status} {date}  <b>{label}</b>  (#{s['id']})")

    lines.append("\nДля деталей тренировки: /session &lt;номер&gt;")
    await message.answer("\n".join(lines), parse_mode="HTML")


@router.message(Command("session"))
async def cmd_session_detail(message: Message):
    parts = message.text.strip().split()
    if len(parts) < 2 or not parts[1].isdigit():
        await message.answer("Использование: /session &lt;номер&gt;\nПример: /session 3", parse_mode="HTML")
        return

    session_id = int(parts[1])
    logs = await db.get_exercises_for_session(session_id)
    if not logs:
        await message.answer("Тренировка не найдена или не содержит записей.")
        return

    lines = [f"<b>Тренировка #{session_id}</b>\n"]
    for log in logs:
        sets = json.loads(log["sets_json"] or "[]")
        sets_str = "  |  ".join(sets) if sets else "—"
        lines.append(f"• <b>{log['exercise_name']}</b>\n  {sets_str}")

    await message.answer("\n".join(lines), parse_mode="HTML")


@router.message(F.text.in_({"📊 Статистика", "/stats"}))
async def cmd_stats(message: Message):
    user_id = message.from_user.id
    sessions = await db.get_last_sessions(user_id, limit=100)
    user_state = await db.get_user_state(user_id)

    total = len(sessions)
    completed = sum(1 for s in sessions if s["completed_at"])

    if user_state:
        week = user_state["current_week"]
        from workouts import week_to_phase
        phase = week_to_phase(week)
        phase_info = f"Неделя <b>{week}</b> / Фаза <b>{phase}</b>"
    else:
        phase_info = "Программа ещё не начата"

    text = (
        f"<b>📊 Общая статистика</b>\n\n"
        f"{phase_info}\n"
        f"Всего тренировок: <b>{total}</b>\n"
        f"Завершено: <b>{completed}</b>\n\n"
        "Для просмотра прогресса по упражнению:\n"
        "/progress &lt;название упражнения&gt;\n\n"
        "Или нажми кнопку ниже для выбора упражнения:"
    )

    await message.answer(text, reply_markup=stats_kb(), parse_mode="HTML")


@router.message(Command("progress"))
async def cmd_progress(message: Message):
    parts = message.text.split(maxsplit=1)
    if len(parts) < 2:
        await _ask_exercise_name(message)
        return
    await _show_exercise_progress(message, message.from_user.id, parts[1].strip())


@router.callback_query(F.data == "pick_exercise_progress")
async def cb_pick_exercise(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    user_id = callback.from_user.id
    names = await db.get_all_exercise_names(user_id)
    if not names:
        await callback.message.answer("Нет данных для анализа. Сначала проведи тренировку!")
        return

    # Показываем список упражнений с номерами
    lines = ["<b>Выбери упражнение (напиши номер или название):</b>\n"]
    for i, name in enumerate(names, 1):
        lines.append(f"{i}. {name}")

    await callback.message.answer("\n".join(lines), parse_mode="HTML")
    await state.set_state(StatsStates.waiting_for_exercise_name)
    await state.update_data({"exercise_list": names})


@router.message(StatsStates.waiting_for_exercise_name)
async def handle_exercise_pick(message: Message, state: FSMContext):
    data = await state.get_data()
    names = data.get("exercise_list", [])
    text = message.text.strip()

    if text.isdigit():
        idx = int(text) - 1
        if 0 <= idx < len(names):
            name = names[idx]
        else:
            await message.answer("Неверный номер. Попробуй ещё раз.")
            return
    else:
        # Ищем по частичному совпадению
        matches = [n for n in names if text.lower() in n.lower()]
        if len(matches) == 1:
            name = matches[0]
        elif len(matches) > 1:
            lines = ["Найдено несколько совпадений, уточни:\n"] + [f"• {m}" for m in matches]
            await message.answer("\n".join(lines))
            return
        else:
            await message.answer(f"Упражнение «{text}» не найдено. Попробуй ещё раз.")
            return

    await state.clear()
    await _show_exercise_progress(message, message.from_user.id, name)


async def _ask_exercise_name(message: Message):
    await message.answer(
        "Укажи название упражнения:\n<code>/progress Tuck front lever hold</code>\n\n"
        "Или нажми «📊 Статистика» и выбери упражнение из списка.",
        parse_mode="HTML",
    )


async def _show_exercise_progress(message: Message, user_id: int, exercise_name: str):
    history = await db.get_exercise_history(user_id, exercise_name)

    if not history:
        await message.answer(f"Нет данных по упражнению «{exercise_name}».")
        return

    lines = [f"<b>📈 {exercise_name}</b>\n"]
    for entry in history:
        date = _fmt_date(entry["started_at"])
        sets = json.loads(entry["sets_json"] or "[]")
        sets_str = "  |  ".join(sets) if sets else "—"
        lines.append(f"<code>{date}</code>  {sets_str}")

    # Простой анализ: сравниваем первую и последнюю запись
    if len(history) >= 2:
        first_sets = json.loads(history[0]["sets_json"] or "[]")
        last_sets = json.loads(history[-1]["sets_json"] or "[]")
        analysis = _analyze_progress(first_sets, last_sets)
        if analysis:
            lines.append(f"\n{analysis}")

    await message.answer("\n".join(lines), parse_mode="HTML")


def _analyze_progress(first: list, last: list) -> str:
    """Простой анализ: сравнивает числа из первой и последней записи."""
    def extract_numbers(sets: list) -> list[float]:
        nums = []
        for s in sets:
            for token in str(s).replace("×", " ").split():
                token = token.replace("+", "").replace("кг", "").replace("сек", "")
                try:
                    nums.append(float(token))
                except ValueError:
                    pass
        return nums

    first_nums = extract_numbers(first)
    last_nums = extract_numbers(last)

    if not first_nums or not last_nums:
        return ""

    avg_first = sum(first_nums) / len(first_nums)
    avg_last = sum(last_nums) / len(last_nums)

    if avg_last > avg_first * 1.05:
        return "✅ Есть прогресс!"
    elif avg_last < avg_first * 0.95:
        return "⚠️ Результаты снизились."
    else:
        return "➡️ Результаты стабильны."


@router.message(Command("week"))
async def cmd_set_week(message: Message):
    parts = message.text.strip().split()
    if len(parts) < 2 or not parts[1].isdigit():
        await message.answer("Использование: /week &lt;номер&gt;\nПример: /week 5", parse_mode="HTML")
        return

    week = int(parts[1])
    if not 1 <= week <= 12:
        await message.answer("Неделя должна быть от 1 до 12.")
        return

    user_id = message.from_user.id
    from workouts import week_to_phase, phase_start_index
    phase = week_to_phase(week)
    next_idx = phase_start_index(phase)
    await db.update_user_state(user_id, current_week=week, next_workout_index=next_idx)
    await message.answer(
        f"✅ Установлена неделя <b>{week}</b> (Фаза <b>{phase}</b>). "
        "Следующая тренировка начнётся с первой тренировки этой фазы.",
        parse_mode="HTML",
    )
