from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from lexicons.lexicon import START_TEST_BTN

# Функция для создания кнопок ответов
async def get_answer_buttons(answers: dict):
    keyboard = [                                  # Создаем список кнопок
        [InlineKeyboardButton(text=key, callback_data=f"answ_{str(value)}")]  # Каждая кнопка с текстом и True/False
        for key, value in answers.items()
    ]
    return InlineKeyboardMarkup(inline_keyboard=keyboard)  # Возвращаем разметку для сообщений

async def get_menu_keyboard():
    start_test_btn = KeyboardButton(text=START_TEST_BTN)  # Кнопка для старта теста
    menu_buttons = ReplyKeyboardMarkup(  # Клавиатура с одной кнопкой
        keyboard=[[start_test_btn]],  # Кнопка в одном ряду
        resize_keyboard=True  # Подстраиваем размер под экран
    )
    return menu_buttons
