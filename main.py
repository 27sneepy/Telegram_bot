from itertools import count

from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, BotCommand, ReplyKeyboardRemove, \
    InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from asyncio import run
from config import BOT_TOKEN
from aiogram.filters import Command

async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    start_test_btn=KeyboardButton(text="Начать тест")
    menu_buttons=ReplyKeyboardMarkup(keyboard=[[start_test_btn]])
    questions=[{"Какое из этих семи чудес света находилось в Египте и сохранилось до наших дней?":"Пирамида Хеопса"},
               {"Как звали французскую героиню, ставшую символом освобождения во время Столетней войны?":"Жанна д’Арк"},
               {"Какой мореплаватель возглавил первую в истории экспедицию, совершившую кругосветное путешествие?":"Фернан Магеллан"}]

    @dp.message(Command(commands=["start"]))
    async def start_handler(message: Message):
        await message.answer("Нажмите кнопку, чтобы начать тест", reply_markup=menu_buttons)

    @dp.message(F.text=="Начать тест")
    async def menu_handler(message: Message):
        answ=list(questions[0].keys())[0]
        text=list(questions[0].values())[0]
        answ_1_btn=InlineKeyboardButton(text=text,callback_data="question_1")
        answ_kb=InlineKeyboardMarkup(inline_keyboard=[[answ_1_btn]])
        await message.answer(answ[0], reply_markup=answ_kb)

    @dp.callback_query(F.data=="question")
    async def answ_handler(callback: CallbackQuery):
        nonlocal counter
        counter +=1
        answ=list(questions[counter].keys())[0]
        text=list(questions[counter].values())[0]
        answ_1_btn=InlineKeyboardButton(text=text,callback_data="question")
        answ_kb=InlineKeyboardMarkup(inline_keyboard=[[answ_1_btn]])
        await callback.message.answer(text=answ, reply_markup=answ_kb)



    await dp.start_polling(bot)
print(f'[LOG] Бот запущен')
run(main())
