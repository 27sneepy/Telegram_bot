from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def services_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="Маникюр", callback_data="service_manicure"),
            InlineKeyboardButton(text="Стрижка", callback_data="service_haircut")
        ],
        [
            InlineKeyboardButton(text="Массаж", callback_data="service_massage")
        ]
    ])


def signup_keyboard(service_name: str):
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Записаться",
                callback_data=f"signup_{service_name}"
            )
        ]
    ])