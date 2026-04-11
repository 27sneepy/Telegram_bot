from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from keyboards.inline import services_keyboard
from lexicons.lexicon import START_TEXT

router = Router()

@router.message(Command("start"))
async def start_handler(message: Message):
    await message.answer(START_TEXT, reply_markup=services_keyboard())