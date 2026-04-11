from aiogram import Bot, Dispatcher
from configs.config import BOT_TOKEN
from asyncio import run
from handlers import start, services

async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    dp.include_router(start.router)
    dp.include_router(services.router)

    await dp.start_polling(bot)

run(main())