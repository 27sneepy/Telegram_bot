from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message
from asyncio import run
from config import BOT_TOKEN


async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()
    # https://catfact.ninja/fact
    @dp.message(Command(commands=['start']))
    async def start_handler(message: Message):
        print(f"[LOG] пользователь {message.from_user.id, message.from_user.first_name} нажал на кнопку старт")

        await message.answer(f'Привет {message.from_user.full_name}')
    @dp.message()
    async def get_cat_fact(message: Message):
        await dp.start_polling(bot)
        print(f'[LOG] Бот запущен')
if __name__ == 'main':
    run(main()) # запускает цикла событий(dispatcher)