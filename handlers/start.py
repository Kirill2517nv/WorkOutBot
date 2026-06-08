from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart, Command

from keyboards import main_menu_kb

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        "Привет! 💪 Я твой бот для тренировок по программе калистеники.\n\n"
        "<b>Что я умею:</b>\n"
        "• Вести тебя по тренировке упражнение за упражнением\n"
        "• Сохранять результаты каждого подхода\n"
        "• Показывать историю тренировок и прогресс\n\n"
        "<b>Команды:</b>\n"
        "/train — начать тренировку\n"
        "/history — последние 10 тренировок\n"
        "/stats — общая статистика\n"
        "/progress &lt;упражнение&gt; — прогресс по упражнению\n"
        "/week &lt;номер&gt; — установить текущую неделю (1–12)\n"
        "/session &lt;номер&gt; — детали конкретной тренировки\n\n"
        "Нажми <b>🏋️ Начать тренировку</b> чтобы начать!",
        reply_markup=main_menu_kb(),
        parse_mode="HTML",
    )


@router.message(F.text == "ℹ️ Помощь")
async def cmd_help(message: Message):
    await message.answer(
        "<b>Как пользоваться ботом:</b>\n\n"
        "1. Нажми <b>🏋️ Начать тренировку</b>\n"
        "2. Выполни упражнение и введи результат\n"
        "3. Бот покажет следующее упражнение\n\n"
        "<b>Форматы ввода:</b>\n"
        "• Время: <code>10 11 9 10</code> (секунды каждого подхода)\n"
        "• Повторения: <code>8 7 6 6</code>\n"
        "• С весом: <code>6×+10 5×+10 5×+10</code>\n"
        "• Бег: просто число минут — <code>30</code>\n\n"
        "<b>Кнопки во время тренировки:</b>\n"
        "• ⏭ Пропустить — если не смог сделать упражнение\n"
        "• 🛑 Завершить — остановить тренировку досрочно\n\n"
        "<b>Прогресс:</b>\n"
        "/progress Tuck front lever hold — динамика по упражнению\n"
        "/week 5 — если ты уже на 5-й неделе",
        parse_mode="HTML",
    )
