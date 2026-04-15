from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from lexicons.lexicon import LIST_COURSES,JOIN_TEXTS

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

async def join_course():
    list_btns=[]
    for key,value in JOIN_TEXTS.items():
        button=InlineKeyboardButton(text=key,callback_data=value)
        list_btns.append([button])
    keyboard=InlineKeyboardMarkup(
        inline_keyboard=list_btns
        )
    return keyboard