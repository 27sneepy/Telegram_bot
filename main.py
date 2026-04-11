from aiogram import Bot, Dispatcher  # Импортируем бота, диспетчер и фильтры
from asyncio import run                  # Для запуска асинхронной функции
from handlers import router
from configs.config import BOT_TOKEN             # Токен вашего бота из config.py

# Основная функция бота
async def main():
    bot = Bot(token=BOT_TOKEN)                          # Создаем объект бота
    dp = Dispatcher()                                   # Создаем диспетчер

    dp.include_router(router)

    # Запуск бота
    await dp.start_polling(bot)  # Начинаем опрос Telegram API
# Точка входа
print('[LOG] Бот запущен')   # Лог запуска
run(main())                   # Запускаем асинхронную функцию main
# as