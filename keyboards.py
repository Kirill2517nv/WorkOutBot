from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton


def main_menu_kb() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="🏋️ Начать тренировку")],
            [KeyboardButton(text="📊 Статистика"), KeyboardButton(text="📅 История")],
            [KeyboardButton(text="ℹ️ Помощь")],
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


def stats_kb() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="📈 Прогресс по упражнению", callback_data="pick_exercise_progress")],
        ]
    )
