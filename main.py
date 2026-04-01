from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, BotCommand, ReplyKeyboardRemove, \
    InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from asyncio import run
from config import BOT_TOKEN
from aiogram.filters import Command
import asyncio

async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    # InlineKeyboardMarkup клавиатура
    # InlineKeyboardButton кнопки

    btn_1=InlineKeyboardButton(text="Пицца",callback_data="пицца")
    btn_2 = InlineKeyboardButton(text="Американские бургеры", callback_data="бургеры")
    keyboard=InlineKeyboardMarkup(inline_keyboard=[[btn_1], [btn_2]])

    @dp.message(F.text=="заказ")
    async def start(message: Message):
        await message.answer(text="Выберите блюдо", reply_markup=keyboard)

    @dp.callback_query(F.data)
    async def callback_handler(callback: CallbackQuery):
        data = callback.data
        await callback.message.edit_text(f"Вы выбрали: {data}")
        await asyncio.sleep(1)
        await callback.answer("Оформляем заказ...")
        await asyncio.sleep(1)
        await callback.message.edit_text("Ожидание курьера...")
        await asyncio.sleep(1)
        await callback.message.edit_text(f"{data} - заказ готов")

    await dp.start_polling(bot)
print(f'[LOG] Бот запущен')
# if name == '__main__':
run(main()) # запускает цикла событий(dispatcher)
