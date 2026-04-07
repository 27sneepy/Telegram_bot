from aiogram import Bot, Dispatcher, F  # Импортируем бота, диспетчер и фильтры
from aiogram.types import (             # Импортируем типы сообщений и кнопок
    Message, ReplyKeyboardMarkup, KeyboardButton,
    InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
)
from asyncio import run                  # Для запуска асинхронной функции
from config import BOT_TOKEN             # Токен вашего бота из config.py
from aiogram.filters import Command      # Для фильтра команды /start

# Основная функция бота
async def main():
    bot = Bot(token=BOT_TOKEN)                          # Создаем объект бота
    dp = Dispatcher()                                   # Создаем диспетчер

    start_test_btn = KeyboardButton(text="Начать тест") # Кнопка для старта теста
    menu_buttons = ReplyKeyboardMarkup(                # Клавиатура с одной кнопкой
        keyboard=[[start_test_btn]],                    # Кнопка в одном ряду
        resize_keyboard=True                             # Подстраиваем размер под экран
    )

    # Список вопросов и ответов
    questions = [                                      # Каждый вопрос – словарь
        {
            "question": "Какое из этих семи чудес света находилось в Египте и сохранилось до наших дней?",
            "answers": {"Пирамида Хеопса": True, "Колосс Родосский": False, "Висячие сады Семирамиды": False}
        },
        {
            "question": "Как звали французскую героиню, ставшую символом освобождения во время Столетней войны?",
            "answers": {"Жанна д’Арк": True, "Екатерина Медичи": False, "Мария-Антуанетта": False}
        },
        {
            "question": "Какой мореплаватель возглавил первую в истории экспедицию, совершившую кругосветное путешествие?",
            "answers": {"Фернан Магеллан": True, "Христофор Колумб": False, "Васко да Гама": False}
        }
    ]

    counter = 0   # Номер текущего вопроса
    score = 0     # Количество правильных ответов

    # Функция для создания кнопок ответов
    async def get_answer_buttons(answers: dict):
        keyboard = [                                  # Создаем список кнопок
            [InlineKeyboardButton(text=key, callback_data=f"answ_{str(value)}")]  # Каждая кнопка с текстом и True/False
            for key, value in answers.items()
        ]
        return InlineKeyboardMarkup(inline_keyboard=keyboard)  # Возвращаем разметку для сообщений

    # Обработка команды /start
    @dp.message(Command("start"))
    async def start_handler(message: Message):
        await message.answer("Нажмите кнопку, чтобы начать тест", reply_markup=menu_buttons)  # Показываем стартовую клавиатуру

    # Начало теста
    @dp.message(F.text == "Начать тест")
    async def start_test_handler(message: Message):
        nonlocal counter, score
        counter = 0                                    # Сбрасываем счетчик вопросов
        score = 0                                      # Сбрасываем счет правильных ответов

        quest = questions[counter]["question"]         # Берем текст первого вопроса
        buttons = questions[counter]["answers"]        # Берем варианты ответов
        keyboard = await get_answer_buttons(buttons)   # Генерируем кнопки

        await message.answer(quest, reply_markup=keyboard)  # Отправляем вопрос с кнопками

    # Обработка нажатий на ответы
    @dp.callback_query(F.data.startswith("answ_"))
    async def answer_handler(callback: CallbackQuery):
        nonlocal counter, score

        is_correct = callback.data.split("_")[1] == "True"  # Проверяем правильность ответа

        if is_correct:
            score += 1
            await callback.message.answer("Правильно!")   # Сообщение при верном ответе
        else:
            await callback.message.answer("Неправильно!") # Сообщение при неверном ответе

        counter += 1                                        # Переходим к следующему вопросу

        if counter >= len(questions):                      # Если вопросы закончились
            await callback.message.answer(f"Тест завершён! Ваш результат: {score}/{len(questions)}")  # Показываем результат
            return

        # Показываем следующий вопрос
        quest = questions[counter]["question"]
        buttons = questions[counter]["answers"]
        keyboard = await get_answer_buttons(buttons)

        await callback.message.answer(quest, reply_markup=keyboard)

    # Запуск бота
    await dp.start_polling(bot)  # Начинаем опрос Telegram API

# Точка входа
print('[LOG] Бот запущен')   # Лог запуска
run(main())                   # Запускаем асинхронную функцию main