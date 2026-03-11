from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from asyncio import run
from config import BOT_TOKEN

ids = []
async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    @dp.message(~F.from_user.id.in_(ids))
    async def id_handler(message: Message):
        ids.append(message.from_user.id)
        await message.answer("привет новичок")
    @dp.message(F.from_user.id.in_(ids))
    async def id_handler(message: Message):
        await message.answer("рад тебя снова видеть")
    await dp.start_polling(bot)
if __name__ == '__main__':
    run(main())