from aiogram import Router
from aiogram.types import CallbackQuery

from keyboards.inline import signup_keyboard
from lexicons.lexicon import SERVICES_TEXT, SUCCESS_TEXT

router = Router()

@router.callback_query()
async def callbacks_handler(callback: CallbackQuery):
    data = callback.data

    if data.startswith("service_"):
        service_name = data.split("_")[1]

        await callback.message.edit_text(
            SERVICES_TEXT[service_name],
            reply_markup=signup_keyboard(service_name)
        )

    elif data.startswith("signup_"):
        await callback.message.edit_text(SUCCESS_TEXT)