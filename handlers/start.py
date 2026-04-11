from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from lexicons.lexicon import START_TEXT

router = Router()

@router.message(Command("start"))
async def start_handler(message: Message):
    await message.answer(START_TEXT)