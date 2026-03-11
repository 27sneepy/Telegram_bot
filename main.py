from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from asyncio import run
from config import BOT_TOKEN
import os

async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    # @dp.message(F.photo)
    # async def get_photo(message: Message, bot: Bot):
    #     print(f"[LOG] пользователь {message.from_user.id} вызвал функцию get_photo")
    #     photo=message.photo[-1]
    #     file = await bot.get_file(photo.file_id)
    #     print(f"[LOG] получение файла {file.file_name}")
    #     PATH=os.path.join("files",f"{file.file_unique_id}.jpg")
    #     print(PATH)
    #     await bot.download_file(file.file_path,destination=PATH)
    #     print(f"[LOG] сохранение файла {PATH}")
    #     print(file)
    #     await message.answer("cool photo")
    @dp.message(F.photo | F.video)
    async def get_photo_video(message: Message, bot: Bot):
        print(f"[LOG] Пользователь {message.from_user.id} вызвал функцию get_photo_video")
        os.makedirs("downloads", exist_ok=True)
        if not message.photo:
            file = await bot.get_file(message.video.file_id)
            print(f'[LOG] Файл {file.file_unique_id} получен')
            PATH = os.path.join("downloads", f"{file.file_unique_id}.jpg")

        else:
            file = await bot.get_file(message.photo[-1].file_id)
            print(f'[LOG] Файл {file.file_unique_id} получен')
            PATH = os.path.join("downloads", f"{file.file_unique_id}.mp4")

        await bot.download_file(file.file_path, destination=PATH)
        print(f'[LOG] Файл {PATH} сохранен в соответствующую директорию')

        await message.answer("крутое фото или видео")

    await dp.start_polling(bot)

print(f'[LOG] Бот запущен')

if __name__ == '__main__':
    run(main()) # запускает цикла событий(dispatcher)