from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message
from requests import get
from asyncio import run
from config import BOT_TOKEN


async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()
    @dp.message(Command(commands=['start']))
    async def start_handler(message: Message):
        print(f"[LOG] пользователь {message.from_user.id, message.from_user.first_name} нажал на кнопку старт")
        await message.answer(f'Привет {message.from_user.full_name}')
    @dp.message(Command(commands=['catfact']))
    async def get_cat_fact(message: Message):
        print(f"[LOG] Пользователь {message.from_user.id} нажал команду /catfact")
        print(f"[LOG] Запрашиваю факт о котах")
        response = get('https://catfact.ninja/fact')
        print(f"[LOG] получен результат со статусом {response.status_code}")
        response_json = response.json()
        print(response_json["fact"])
        await message.answer(response_json["fact"])

    @dp.message(Command(commands=['breeds']))
    async def breeds_handler(message: Message):
        result=get("https://catfact.ninja/breeds")
        result_json = result.json()
        print(result_json["data"][0]["country"])
        print(result_json["data"][0]["breed"])
        await message.answer(result_json["data"][0]["country"])


    @dp.message(F.text)
    async def random_answer(message: Message):
        print(f"[LOG] Пользователь {message.from_user.id} написал текст: {message.text}")
        await message.answer("!!!")


    await dp.start_polling(bot)

print(f'[LOG] Бот запущен')

if __name__ == '__main__':
    run(main()) # запускает цикла событий(dispatcher)