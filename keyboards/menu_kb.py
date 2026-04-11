from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from lexicons.lexicon import LIST_COURSES

async def menu_kb():
    list_btns=[]
    for key,value in LIST_COURSES.items():
        button=InlineKeyboardButton(
            text=key,callback_data=value
        )
        list_btns.append([button])
    keyboards=InlineKeyboardMarkup(
        inline_keyboard=list_btns
    )
    return keyboards