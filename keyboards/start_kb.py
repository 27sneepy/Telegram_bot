from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from lexicons.lexicon import START_BUTTON_TEXT

async def start_kb():
    list_bts=[]
    for text in START_BUTTON_TEXT:
        button1=KeyboardButton(text=text)
        list_bts.append([button1])
    keyboards=ReplyKeyboardMarkup(keyboard=list_bts)
    return keyboards