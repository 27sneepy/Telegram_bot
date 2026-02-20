# import requests
# import asyncio
# from config import Config, load_config, TgBot
# from aiogram import Bot, Dispatcher
# from aiogram.filters import Command
# from aiogram.types import Message
#
# config: Config = load_config(".env")
# bot_token = config.bot.token
#
# bot = Bot(token=bot_token)
#
# dp = Dispatcher()
#
# @dp.message(Command(commands=["start"]))
# async def process_start(message: Message):
#     await message.answer("Привет!")
#
# # help
# @dp.message(Command(commands=["help"]))
# async def process_help(message: Message):
#     await message.answer("Команды:\n/start - Старт \n/help - О боте")
#
#
# @dp.message(Command(commands=['dog']))
# async def answer_dog(message: Message):
#     s = requests.get("https://dog.ceo/api/breeds/image/random")
#     print(s.content)
#
# async def main():
#     bot = Bot(token=bot_token)
#     dp = Dispatcher()
#     await dp.start_polling(bot)
# #
# if __name__ == '__main__':
#     asyncio.run(main())

import asyncio
import aiohttp
from config import Config, load_config
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

config: Config = load_config(".env")
bot_token = config.bot.token


async def main():
    bot = Bot(token=bot_token)
    dp = Dispatcher()

    @dp.message(Command(commands=["start"]))
    async def process_start(message: Message):
        await message.answer("Привет!")

    @dp.message(Command(commands=["help"]))
    async def process_help(message: Message):
        await message.answer("Команды:\n/start\n/help\n/dog")

    @dp.message(Command(commands=["dog"]))
    async def answer_dog(message: Message):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://dog.ceo/api/breeds/image/random") as response:
                data = await response.json()
                dog_url = data["message"]

        await message.answer_photo(dog_url)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())