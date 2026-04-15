from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from keyboards.menu_kb import menu_kb, join_course
from lexicons.lexicon import START_BUTTON_TEXT, COURSES_TEXT, COURSES_INFO
from aiogram.fsm.state import State,StatesGroup

class Registration(StatesGroup):
    waiting_name=State()
    waiting_username=State()

router=Router()

@router.message(F.text==START_BUTTON_TEXT[0])
async def courses_handler(message: Message):
    await message.answer(text=COURSES_TEXT,reply_markup=await menu_kb())

@router.callback_query(F.data.startswith("course_"))
async def courses_handler(query: CallbackQuery):
    key=query.data
    info_text= COURSES_INFO[key]
    keyboard=await join_course()
    await query.message.edit_text(info_text, reply_markup=keyboard)

@router.callback_query(F.data=="signup")
async def signup_handler(query: CallbackQuery,state: FSMContext):
    await query.message.answer("Введите ФИО:")
    await state.set_state(Registration.waiting_name)

@router.message(Registration.waiting_name)
async def process_name(message: Message,state: FSMContext):
    await message.answer("Введите username")
    await state.update_data(name=message.text)
    await state.set_state(Registration.waiting_username)

@router.message(Registration.waiting_username)
async def process_username(message: Message,state: FSMContext):
    state_data = await state.get_data()
    name = state_data.get("name","undefined")

    await message.answer(
        f"Ваше имя {name}\nВаш юзернейм {message.text}"
    )
    await state.set_state(None) # заканчивает состояние
    await state.clear() # очищает все данные и состояния