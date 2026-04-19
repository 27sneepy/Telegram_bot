from aiogram import F, Router, Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from keyboards.menu_kb import menu_kb, join_course
from lexicons.lexicon import START_BUTTON_TEXT, COURSES_TEXT, COURSES_INFO
from aiogram.fsm.state import State,StatesGroup

class Registration(StatesGroup):
    waiting_FIO=State()
    waiting_class_school=State()

router=Router()

@router.message(F.text==START_BUTTON_TEXT[0])
async def courses_handler(message: Message):
    await message.answer(text=COURSES_TEXT,reply_markup=await menu_kb())

@router.callback_query(F.data.startswith("course_"))
async def courses_handler(query: CallbackQuery,state: FSMContext):
    key=query.data
    await state.update_data(course=key[7:])
    info_text= COURSES_INFO[key]
    keyboard=await join_course()
    await query.message.edit_text(info_text, reply_markup=keyboard)

@router.callback_query(F.data=="back")
async def back_handler(query: CallbackQuery):
    await query.message.edit_text(text=COURSES_TEXT,reply_markup=await menu_kb())



@router.callback_query(F.data=="signup")
async def signup_handler(query: CallbackQuery,state: FSMContext):
    await query.message.answer("Введите ФИО:")
    await state.set_state(Registration.waiting_FIO)



@router.message(Registration.waiting_FIO)
async def process_name(message: Message,state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Введите класс и школу:")
    await state.set_state(Registration.waiting_class_school)



@router.message(Registration.waiting_class_school)
async def process_school(message: Message,state: FSMContext,bot:Bot):
    await state.update_data(school=message.text)
    state_data = await state.get_data()
    name = state_data.get("name","undefined")
    school = state_data.get("clas", "undefined")
    course = state_data.get("course", "undefined")

    await message.answer(
        f"Ваше имя: {name}\nВаш класс и школа: {school}\nВаш курс: {course}"
    )
    await bot.send_message(
        chat_id=message.chat.id,
        text=f"Ваше имя: {name}\nВаш класс и школа: {school}\nВаш курс: {course}"
    )
    await state.set_state(None) # заканчивает состояние
    await state.clear() # очищает все данные и состояния

