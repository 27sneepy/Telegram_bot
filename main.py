from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup, BotCommand
from asyncio import run
from config import BOT_TOKEN
import os
from aiogram.filters import Command
import asyncio
import random
async def set_commands(bot: Bot):
    commands = [
        BotCommand(command='/start', description="эта команда начинает бот"),

    ]
    await bot.set_my_commands(commands)
async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()
    await set_commands(bot)



    button1=KeyboardButton(text="Команда 1")
    button2=KeyboardButton(text="Команда 2")
    button3=KeyboardButton(text="отправь мне фото")
    keyboard=ReplyKeyboardMarkup(keyboard=[[button1,button2,button3]], # формируем клавиатуру
                                 resize_keyboard=True, # сжатие кнопки до высоты текста (и ширины экрана телефона)
                                 input_field_placeholder="Клавиатура есть в плейсхолдере",
                                 is_persistent=True)

    @dp.message(Command(commands="start"))
    async def start_handler(message: Message):
        await message.answer(text="выбери команду", reply_markup=keyboard)


    @dp.message(F.text == "Команда 1")
    async def command1_handler(message: Message):
        await message.answer(text="ты выбрал 1 команду")

    @dp.message(F.text == "Команда 2")
    async def command2_handler(message: Message):
        print(f"[LOG] команда command_handler была запущена")
        await message.answer(text="ты выбрал 2 команду")
        print(f"[LOG] команда command_handler была завершена")

    @dp.message(F.text == "отправь мне фото")
    async def command3_handler(message: Message):
        await message.answer_photo(photo="https://cameralabs.org/media/k2/items/cache/ff3d1376bcf78907b7cd02699415ecae_L.jpg")


    await dp.start_polling(bot)
print(f'[LOG] Бот запущен')
if __name__ == '__main__':
    run(main()) # запускает цикла событий(dispatcher)