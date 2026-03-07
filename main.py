from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message
from requests import get
from asyncio import run
from config import BOT_TOKEN
from random import choice

async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    # F - встроено все что нам нужно
    # Command - ограничение
    # CommandStart - ограничение

    # @dp.message(F.from_user.username.contains("a"))
    # async def echo(message: Message):
    #     await message.answer("привет")
    a=[5059184679,12312321]
    @dp.message(F.from_user.id.in_(a),Command(commands=["secret"]))
    async def echo(message: Message):
        await message.answer("Привет")

    # @dp.message(F.text.in_("start"))
    # async def handler(message: Message):
    #     await message.answer("asda")
    #
    # # содержится в сообщении start
    # @dp.message(F.text.contains("start"))
    # async def handler(message: Message):
    #     await message.answer(f"ПРивет {message.from_user.first_name}")
    #
    # @dp.message(F.from_user.username == ("weshouldnttalkanymore"))
    # async def handler(message: Message):
    #     await message.answer("sdasd")
    #
    #
    # @dp.message(Command(commands=['start']))
    # async def start_handler(message: Message):
    #     print(f"[LOG] пользователь {message.from_user.id, message.from_user.first_name} нажал на кнопку старт")
    #     await message.answer(f'Привет {message.from_user.full_name}')



    await dp.start_polling(bot)

print(f'[LOG] Бот запущен')

if __name__ == '__main__':
    run(main()) # запускает цикла событий(dispatcher)