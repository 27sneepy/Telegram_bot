from base64 import bytes_types

from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, BotCommand, ReplyKeyboardRemove, \
    InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from asyncio import run
from config import BOT_TOKEN
from aiogram.filters import Command

async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()
    # Реализуй команду /menu она должна появиться в меню и при нажатии на нее отображается
    # сообщение "Выбери действие" с inline кнопками
    # "счетчик" - при нажатии на эту кнопку отправляется число 0 и 2 inline
    # кнопки +  и  -, при нажатии на + прибавляется 1 к значению при нажатии
    # на -- убавляется на 1 значение и обновляется сообщение
    # "решение" - при нажатии на кнопку переходишь на другой сайт или группу (любая ссылка)
    btn1=InlineKeyboardMarkup(text="счетчик",callback_data="счетчик")
    kb = (InlineKeyboardMarkup(inline_keyboard=[[btn1]])
    @dp.message(Command(commands=['menu'])))
    async def menu(message: Message):
        await message.answer("Выбери действие",reply_markup=kb)


    await dp.start_polling(bot)
print(f'[LOG] Бот запущен')
run(main())
