from aiogram import Router, F
from aiogram.types import Message, CallbackQuery

from workouts import WORKOUTS
from keyboards import program_phases_kb, program_days_kb

router = Router()

PHASE_DESCRIPTIONS = {
    1: "Фундамент (недели 1–4)\nОсвоить паттерны движений, выстроить компрессию, убрать судороги в L-sit.\nЦели: Tuck FL, Tuck BL, Frog stand, Tuck L-sit",
    2: "Прогрессия (недели 5–8)\nВыйти на advanced tuck FL и BL, первые tuck planche holds, стабильный full L-sit 20+ сек.",
    3: "Финальный пуш (недели 9–12)\nOne-leg или straddle FL, straddle или full BL, advanced tuck PL, L-sit 25+ сек.",
}

DAY_KEYS = {
    (1, "A"): "phase1_A",
    (1, "B"): "phase1_B",
    (1, "C"): "phase1_C",
    (2, "A"): "phase2_A",
    (2, "B"): "phase2_B",
    (2, "C"): "phase2_C",
    (3, "A"): "phase3_A",
    (3, "B"): "phase3_B",
    (3, "C"): "phase3_C",
}


@router.message(F.text == "📋 Программа тренировок")
async def cmd_program(message: Message):
    text = (
        "<b>📋 Программа тренировок — 12 недель</b>\n\n"
        "<b>Расписание:</b> 3 тренировки в неделю\n"
        "Пн — День А  |  Ср — День Б  |  Пт/Сб — День В\n\n"
        "<b>Цели программы:</b> Горизонт (FL), Горизонт сзади (BL), Планш (PL)\n\n"
        "Выбери фазу чтобы посмотреть тренировки:"
    )
    await message.answer(text, reply_markup=program_phases_kb(), parse_mode="HTML")


@router.callback_query(F.data.startswith("prog_phase:"))
async def cb_program_phase(callback: CallbackQuery):
    phase = int(callback.data.split(":")[1])
    desc = PHASE_DESCRIPTIONS[phase]
    text = f"<b>Фаза {phase}</b> — {desc}\n\nВыбери день тренировки:"
    await callback.message.edit_text(text, reply_markup=program_days_kb(phase), parse_mode="HTML")
    await callback.answer()


@router.callback_query(F.data == "prog_back")
async def cb_program_back(callback: CallbackQuery):
    text = (
        "<b>📋 Программа тренировок — 12 недель</b>\n\n"
        "<b>Расписание:</b> 3 тренировки в неделю\n"
        "Пн — День А  |  Ср — День Б  |  Пт/Сб — День В\n\n"
        "<b>Цели программы:</b> Горизонт (FL), Горизонт сзади (BL), Планш (PL)\n\n"
        "Выбери фазу чтобы посмотреть тренировки:"
    )
    await callback.message.edit_text(text, reply_markup=program_phases_kb(), parse_mode="HTML")
    await callback.answer()


@router.callback_query(F.data.startswith("prog_day:"))
async def cb_program_day(callback: CallbackQuery):
    _, phase_str, day = callback.data.split(":")
    phase = int(phase_str)
    workout_key = DAY_KEYS[(phase, day)]
    workout = WORKOUTS[workout_key]

    lines = [f"<b>{workout['title']}</b>\n"]

    # Группируем по секциям
    current_section = None
    section_map = {
        "Бег": "🏃 Разминка",
        "Scapular": "⚡ Скилл-работа",
        "Tuck front": "⚡ Скилл-работа",
        "Tuck back": "⚡ Скилл-работа",
        "Skin": "⚡ Скилл-работа",
        "Front lever": "⚡ Скилл-работа",
        "Back lever": "⚡ Скилл-работа",
        "Planche": "⚡ Скилл-работа",
        "Frog": "⚡ Скилл-работа",
        "Tuck L-sit": "⚡ Скилл-работа",
        "Advanced tuck front": "⚡ Скилл-работа",
        "One-leg front": "⚡ Скилл-работа",
        "Adv. tuck back": "⚡ Скилл-работа",
        "Straddle back": "⚡ Скилл-работа",
        "Tuck planche": "⚡ Скилл-работа",
        "Full L-sit": "⚡ Скилл-работа",
        "FL ": "⚡ Скилл-работа",
        "BL ": "⚡ Скилл-работа",
        "PL ": "⚡ Скилл-работа",
        "One-leg FL": "⚡ Скилл-работа",
        "Straddle BL": "⚡ Скилл-работа",
        "Advanced tuck planche": "⚡ Скилл-работа",
        "Tuck → Adv": "⚡ Скилл-работа",
        "L-sit 25": "⚡ Скилл-работа",
    }

    def get_section(name: str) -> str:
        for prefix, section in section_map.items():
            if name.startswith(prefix):
                return section
        # Силовые vs корпус — определяем по типу
        pull_keywords = ["подтягивани", "Weighted pull", "Chest-to-bar", "Muscle-up",
                         "Австралийские", "Взрывные", "Front lever pull", "Korean"]
        push_keywords = ["Отжимани", "Pike", "Archer", "Weighted dips", "HSPU",
                         "Pseudo planche", "Adv. tuck planche push"]
        core_keywords = ["Подъём прямых ног", "Seated leg", "Hollow body", "L-sit попытки",
                         "Pike compression", "Dragon flag", "Toes-to-bar", "Compression",
                         "L-sit рекорд", "L-sit личный", "L-sit цель", "L-sit на брусьях"]

        name_lower = name.lower()
        for kw in core_keywords:
            if kw.lower() in name_lower:
                return "💪 Корпус"
        return "🔥 Сила"

    for ex in workout["exercises"]:
        section = "🏃 Разминка" if ex["name"] == "Бег" else get_section(ex["name"])
        if section != current_section:
            current_section = section
            lines.append(f"\n<b>{section}</b>")
        lines.append(f"• {ex['name']} — {ex['sets']}×{ex['target']}")

    lines.append(f"\n<i>Всего упражнений: {len(workout['exercises'])}</i>")

    await callback.message.edit_text(
        "\n".join(lines),
        reply_markup=program_days_kb(phase),
        parse_mode="HTML",
    )
    await callback.answer()
