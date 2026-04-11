from aiogram import F, Router
from aiogram.types import Message, InlineKeyboardMarkup
from keyboards.menu_kb import menu_kb
from lexicons.lexicon import START_BUTTON_TEXT, COURSES_TEXT, LIST_COURSES

router=Router()

@router.message(F.text==START_BUTTON_TEXT[0])
async def courses_handler(message: Message):
    await message.answer(text=COURSES_TEXT,reply_markup=await menu_kb())

