from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, BotCommand, ReplyKeyboardRemove, \
    InlineKeyboardMarkup
from asyncio import run
from config import BOT_TOKEN
from aiogram.filters import Command


async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    knopka_1 = KeyboardButton(text='Заказать еду')
    main_keyboard = ReplyKeyboardMarkup(
        keyboard=[[knopka_1]],resize_keyboard=True,input_field_placeholder="Клавиатура есть в плейсходлере ...")

    b1=KeyboardButton(text="пицца")
    b2=KeyboardButton(text="суши")
    back=KeyboardButton(text="назад")
    kb= ReplyKeyboardMarkup(keyboard=[[b1,b2,back]],resize_keyboard=True)

    @dp.message(lambda message: message.text == "/start" or (message.text and message.text.lower() == "назад"))
    async def start(message: Message):
        await message.answer(
            text = "!",
            reply_markup=main_keyboard
        )

    @dp.message(F.text == 'Заказать еду')
    async def com1_handler(message: Message):
        await message.answer(
            text = "!",
            reply_markup=kb
        )

    @dp.message(F.text == 'суши')
    async def get_susi(message: Message):
        await message.answer_photo(photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQphqEqCvFJx7p05cjWyHMJD7Mis6ZOiSXXwg&s")

    @dp.message(F.text == 'пицца')
    async def get_pizza(message: Message):
        await message.answer_photo(
            photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTCy7sZTBqdrSeeB1ChyPoVumMO6_J7haDvuw&s")

    await dp.start_polling(bot)
print(f'[LOG] Бот запущен')
# if name == '__main__':
run(main()) # запускает цикла событий(dispatcher)
