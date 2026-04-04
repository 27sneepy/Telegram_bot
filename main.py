from aiogram import Bot, Dispatcher, F
from aiogram.types import (
    Message, ReplyKeyboardMarkup, KeyboardButton,
    InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
)
from asyncio import run
from config import BOT_TOKEN
from aiogram.filters import Command

async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    start_test_btn = KeyboardButton(text="Начать тест")
    menu_buttons = ReplyKeyboardMarkup(
        keyboard=[[start_test_btn]],
        resize_keyboard=True
    )

    questions = [
        {"Какое из этих семи чудес света находилось в Египте и сохранилось до наших дней?":
            {"Пирамида Хеопса": True, "Колосс Родосский": False, "Висячие сады Семирамиды": False}},
        {"Как звали французскую героиню, ставшую символом освобождения во время Столетней войны?":
            {"Жанна д’Арк": True, "Екатерина Медичи": False, "Мария-Антуанетта": False}},
        {"Какой мореплаватель возглавил первую в истории экспедицию, совершившую кругосветное путешествие?":
            {"Фернан Магеллан": True, "Христофор Колумб": False, "Васко да Гама": False}}
    ]

    counter = 0
    score = 0

    async def get_answ_buttons(btns: dict):
        keyboard = []
        for key, value in btns.items():
            # передаём правильность ответа
            btn = InlineKeyboardButton(
                text=key,
                callback_data=f"answ_{value}"
            )
            keyboard.append([btn])
        return InlineKeyboardMarkup(inline_keyboard=keyboard)

    @dp.message(Command("start"))
    async def start_handler(message: Message):
        await message.answer("Нажмите кнопку, чтобы начать тест", reply_markup=menu_buttons)

    @dp.message(F.text == "Начать тест")
    async def start_test_handler(message: Message):
        nonlocal counter, score
        counter = 0
        score = 0

        quest = list(questions[counter].keys())[0]
        btns_data = questions[counter][quest]
        keyboard = await get_answ_buttons(btns_data)

        await message.answer(quest, reply_markup=keyboard)

    @dp.callback_query(F.data.startswith("answ_"))
    async def answ_handler(callback: CallbackQuery):
        nonlocal counter, score

        # проверяем ответ
        is_correct = callback.data.split("_")[1] == "True"

        if is_correct:
            score += 1
            await callback.message.answer("✅ Правильно!")
        else:
            await callback.message.answer("❌ Неправильно!")

        counter += 1

        # если тест закончился
        if counter >= len(questions):
            await callback.message.answer(f"Тест завершён! Ваш результат: {score}/{len(questions)}")
            return

        # следующий вопрос
        quest = list(questions[counter].keys())[0]
        btns_data = questions[counter][quest]
        keyboard = await get_answ_buttons(btns_data)

        await callback.message.answer(quest, reply_markup=keyboard)

    await dp.start_polling(bot)


print('[LOG] Бот запущен')
run(main())