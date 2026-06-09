from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton


def main_menu_kb() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="🏋️ Начать тренировку")],
            [KeyboardButton(text="📊 Статистика"), KeyboardButton(text="📅 История")],
            [KeyboardButton(text="📋 Программа тренировок"), KeyboardButton(text="ℹ️ Помощь")],
        ],
        resize_keyboard=True,
    )


def exercise_kb() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="⏭ Пропустить упражнение", callback_data="skip_exercise")],
            [InlineKeyboardButton(text="🛑 Завершить тренировку", callback_data="finish_workout")],
        ]
    )


def confirm_finish_kb() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="✅ Да, завершить", callback_data="confirm_finish"),
                InlineKeyboardButton(text="↩️ Продолжить", callback_data="continue_workout"),
            ]
        ]
    )


def week_selection_kb() -> InlineKeyboardMarkup:
    buttons = []
    row = []
    for w in range(1, 13):
        row.append(InlineKeyboardButton(text=str(w), callback_data=f"set_week:{w}"))
        if len(row) == 4:
            buttons.append(row)
            row = []
    if row:
        buttons.append(row)
    return InlineKeyboardMarkup(inline_keyboard=buttons)


def program_phases_kb() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Фаза 1 (нед. 1–4)", callback_data="prog_phase:1"),
                InlineKeyboardButton(text="Фаза 2 (нед. 5–8)", callback_data="prog_phase:2"),
                InlineKeyboardButton(text="Фаза 3 (нед. 9–12)", callback_data="prog_phase:3"),
            ]
        ]
    )


def program_days_kb(phase: int) -> InlineKeyboardMarkup:
    labels = {
        "A": "День А — Тяга",
        "B": "День Б — Толчок",
        "C": "День В — Повтор",
    }
    if phase == 2:
        labels["C"] = "День В — Muscle-up"
    elif phase == 3:
        labels["C"] = "День В — Макс. скиллы"

    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=labels["A"], callback_data=f"prog_day:{phase}:A")],
            [InlineKeyboardButton(text=labels["B"], callback_data=f"prog_day:{phase}:B")],
            [InlineKeyboardButton(text=labels["C"], callback_data=f"prog_day:{phase}:C")],
            [InlineKeyboardButton(text="◀️ Назад к фазам", callback_data="prog_back")],
        ]
    )


def stats_kb() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="📈 Прогресс по упражнению", callback_data="pick_exercise_progress")],
        ]
    )
