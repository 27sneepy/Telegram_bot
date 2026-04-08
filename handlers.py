from aiogram import F, Router  # Импортируем бота, диспетчер и фильтры
from aiogram.types import Message, CallbackQuery # Импортируем типы сообщений и кнопок
from aiogram.filters import Command      # Для фильтра команды /start
from lexicons.lexicon import QUESTIONS,START_TEST_BTN,START_TEST_ANSW
from keyboards.keyboards import get_menu_keyboard,get_answer_buttons

router = Router()
counter = 0   # Номер текущего вопроса
score = 0     # Количество правильных ответов

# Обработка команды /start
@router.message(Command("start"))
async def start_handler(message: Message):
    await message.answer(text=START_TEST_ANSW, reply_markup=await get_menu_keyboard())  # Показываем стартовую клавиатуру

# Начало теста
@router.message(F.text == START_TEST_BTN)
async def start_test_handler(message: Message):
    global counter, score
    counter = 0                                    # Сбрасываем счетчик вопросов
    score = 0                                      # Сбрасываем счет правильных ответов

    quest = QUESTIONS[counter]["question"]         # Берем текст первого вопроса
    buttons = QUESTIONS[counter]["answers"]        # Берем варианты ответов
    keyboard = await get_answer_buttons(buttons)   # Генерируем кнопки

    await message.answer(quest, reply_markup=keyboard)  # Отправляем вопрос с кнопками

# Обработка нажатий на ответы
@router.callback_query(F.data.startswith("answ_"))
async def answer_handler(callback: CallbackQuery):
    global counter, score

    is_correct = callback.data.split("_")[1] == "True"  # Проверяем правильность ответа

    if is_correct:
        score += 1
        await callback.message.answer("Правильно!")   # Сообщение при верном ответе
    else:
        await callback.message.answer("Неправильно!") # Сообщение при неверном ответе

    counter += 1                                        # Переходим к следующему вопросу

    if counter >= len(QUESTIONS):                      # Если вопросы закончились
        await callback.message.answer(f"Тест завершён! Ваш результат: {score}/{len(QUESTIONS)}")  # Показываем результат
        return

    # Показываем следующий вопрос
    quest = QUESTIONS[counter]["question"]
    buttons = QUESTIONS[counter]["answers"]
    keyboard = await get_answer_buttons(buttons)

    await callback.message.answer(quest, reply_markup=keyboard)