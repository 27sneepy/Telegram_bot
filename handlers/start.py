from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from lexicons.lexicon import START_TEXT
from keyboards.start_kb import start_kb

router = Router()

@router.message(Command("start"))
async def start_handler(message: Message):
    # print(message.from_user.id,message.chat.id)
    await message.answer(START_TEXT,reply_markup=await start_kb())