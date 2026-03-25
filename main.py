from aiogram import Bot, Dispatcher, F, types
from aiogram.types import BotCommand, KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import Command
from asyncio import run
from config import BOT_TOKEN

async def set_commands(bot: Bot):
    commands = [
        BotCommand(command='/start', description="старт"),
        BotCommand(command='/about', description="о боте"),
        BotCommand(command='/tasks', description="показать задания"),
    ]
    await bot.set_my_commands(commands)

async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()
    await set_commands(bot)

    # Главное меню клавиатуры
    main_kb = ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text="/tasks"), KeyboardButton(text="/about")]],
        resize_keyboard=True
    )

    # Inline-кнопки для /tasks
    tasks_kb = InlineKeyboardMarkup()
    tasks_kb.add(InlineKeyboardButton("1", callback_data="q"))  # сверху
    tasks_kb.row(
        InlineKeyboardButton("2", callback_data="a"),
        InlineKeyboardButton("3", callback_data="s")
    )

    # /start
    @dp.message(Command("start"))
    async def start(message: types.Message):
        await message.answer(
            "Привет! Я учебный бот.\n\n"
            "Команды:\n"
            "/tasks — показать задания\n"
            "/about — информация обо мне",
            reply_markup=main_kb
        )

    # /about
    @dp.message(Command("about"))
    async def about(message: types.Message):
        await message.answer_photo(
            photo="https://picsum.photos/200",
            caption="Учебный бот\n🌐 https://example.com"
        )

    # /tasks
    @dp.message(Command("tasks"))
    async def tasks_cmd(message: types.Message):
        await message.answer("Выбери действие:", reply_markup=tasks_kb)

    # Обработка кнопок /tasks
    @dp.callback_query(F.data == "q")
    async def question(call: types.CallbackQuery):
        await call.message.answer("❓ Вопрос: 2 + 2 = ?")

    @dp.callback_query(F.data == "a")
    async def answer(call: types.CallbackQuery):
        await call.message.answer("✅ Ответ: 4")

    @dp.callback_query(F.data == "s")
    async def solution(call: types.CallbackQuery):
        await call.message.answer("📘 Решение: складываем 2 + 2 → получаем 4")

    await dp.start_polling(bot)

if __name__ == "__main__":
    print("[LOG] Бот запущен")
    run(main())