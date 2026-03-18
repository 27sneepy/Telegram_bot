from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, FSInputFile
from asyncio import run
from config import BOT_TOKEN
import os
from aiogram.filters import Command
import asyncio
import random

async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()
    # @dp.message(F.photo | F.video | F.voice)
    # async def get_photo_video_voice(message: Message, bot: Bot):
    #     print(f"[LOG] Пользователь {message.from_user.id} вызвал функцию get_photo_video_voice")
    #     os.makedirs("downloads", exist_ok=True)
    #     if message.photo:
    #         file = await bot.get_file(message.photo[-1].file_id)
    #         print(f'[LOG] Файл {file.file_unique_id} получен')
    #         PATH = os.path.join("downloads", f"{file.file_unique_id}.jpg")
    #     elif message.voice:
    #         file = await bot.get_file(message.voice.file_id)
    #         PATH = os.path.join("downloads", f"{file.file_unique_id}.ogg")
    #     else:
    #         file = await bot.get_file(message.video.file_id)
    #         print(f'[LOG] Файл {file.file_unique_id} получен')
    #         PATH = os.path.join("downloads", f"{file.file_unique_id}.mp4")
    #     print(f"[LOG] начало скачивания {file}, по пути {PATH}")
    #     await bot.download_file(file.file_path, destination=PATH)
    #     print(f'[LOG] Файл {PATH} сохранен в соответствующую директорию')
    #
    #     await message.answer("крутое фото или видео или гс")
    # @dp.message(F.sticker)
    # async def get_sticker(message: Message):
    #     print(f"[LOG] пользователь {message.from_user.id} вызвал функцию get_sticker")
    #     with open("stickers.txt", "a+") as f:
    #         f.write(message.sticker.file_id + "\n")
    #         print(f"[LOG] записан стикер {message.sticker.file_id}")
    # @dp.message(F.text == "отправь фото")
    # async def send_photo(message: Message):
    #     print(f"[LOG] получен запрос от {message.from_user.id} в send_photo")
    #     PATH = os.path.join("downloads","123123.jpg")
    #     print(f"[LOG] начало бинаризации")
    #     photo=FSInputFile(PATH)
    #     print(f"[LOG] конец бинаризации")
    #     await message.answer_photo(photo=photo,caption="это география")
    # #     await message.answer_photo("https://ichef.bbci.co.uk/ace/ws/640/cpsprodpb/11582/production/_103424017_mary-mcgowan_caught-in-the-act_00001294.jpg.webp",caption="это белка")
    # @dp.message(Command(commands=["show"]))
    # async def digits_handler(message: Message):
    #     file_name="data.txt"
    #     if not os.path.exists(file_name):
    #         with open(file_name, "w") as f:
    #             f.write("curs temperature\n")
    #             for _ in range(3):
    #                 f.write(f"{random.randint(0, 100)} {random.randint(0, 100)}\n")
    #     with open(file_name, "r") as f:
    #         list_data = f.readlines()
    #         if len(list_data) <= 1:
    #             await message.answer("Нет данных в файле")
    #             return
    #         msg = await message.answer("Загрузка...")
    #         for line in list_data[1:]:
    #             elements = line.split()
    #             await msg.edit_text(f"Текущая температура на улице: {elements[1]}")
    #             await asyncio.sleep(5)
    #         await msg.delete()
    # @dp.message(F.text.lower().endswith("контакт"))
    # async def contact(message: Message):
    #     print(f"[LOG] функция contact запущена")
    #     await message.answer_contact(phone_number="+123123",first_name="adsad")
    #     print(f"[LOG] функция contact завершена")
    # @dp.message(F.text.endswith("адрес"))
    # async def geolocation(message: Message):
    #     print(f"[LOG] функция geolocation запущена")
    #     await message.answer_location(latitude=14,longitude=88)
    #     print(f"[LOG] функция geolocation завершена")
    # @dp.message(Command(commands="start"))
    # async def start_handler(message: Message):
    #     print(f"[LOG] функция start_handler запущена")
    #     await message.answer("Привет")
    #     print(f"[LOG] функция start_handler завершена")
    # @dp.message()
    # async def echo(message: Message):
    #     await message.answer(message.text)
    @dp.message(Command(commands=["silca"]))
    async def silca(message: Message):
        with open("data1.txt", "r") as f:
            file = f.readlines()
            s = await message.answer(f"Загрузка...")
            for i in file[1:]:
                num,link = i.split()
                await s.edit_text(f"для ссылки {link} были загружены данные")
                await asyncio.sleep(5)
    await dp.start_polling(bot)
print(f'[LOG] Бот запущен')
if __name__ == '__main__':
    run(main()) # запускает цикла событий(dispatcher)