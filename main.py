import requests
import asyncio

from aiohttp.hdrs import CONTENT_TYPE

from config import Config, load_config
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, CommandObject, CommandStart, ChatMemberUpdatedFilter,KICKED,MEMBER
from aiogram.types import Message, ChatMemberUpdated , ContentType

config: Config = load_config()
bot_token = config.bot.token

bot = Bot(token=bot_token)

dp = Dispatcher()

def my_help_filter(message: Message)->bool:
    return message.text and message.text.lower() == "/help"

def count_message(message: Message)->bool:
    return message.text and len(message.text)<80


@dp.message(F.text.startswith("Привет"))
async def hello_handler(message: Message):
    await message.answer("Привет")
# ~ инвертирует результат
@dp.message(~F.text.len()<80)
async def short_message_handler(message: Message):
    await message.answer("wow >= 80")
#
@dp.message(F.photo)
async def photo_handler(message: Message):
    # F.photo
    # F.video
    # F.audio
    # F.voice
    # F.document
    # F.sticker
    # F.animation
    # F.contact
    # F.location
    # F.from_user.id
    await message.answer("Nice photo!")

ADMIN_IDS={123,456,789}
@dp.message(F.from_user.id.in_(ADMIN_IDS)) # проверяет принадлежность
async def admin_handler(message: Message):
    await message.answer("Команда для администраторов")

ADMIN_IDS={123,456,789}
@dp.message(F.content_type.in_({ContentType.VIDEO,ContentType.PHOTO})) # проверяет принадлежность
async def media_handler(message: Message):
    await message.answer("медиа")



# @dp.message(Command(commands=["start"],prefix="/"))
@dp.message(CommandStart())
async def process_start(message: Message):
    await message.answer("Привет!")

# изменение со стороны пользователя
@dp.my_chat_member(ChatMemberUpdatedFilter(member_status_changed=KICKED))
async def user_blocked_bot(event: ChatMemberUpdated):
    print(f"Пользователь {event.from_user.id} - {event.from_user.full_name} заблокировал бота")

@dp.my_chat_member(ChatMemberUpdatedFilter(member_status_changed=MEMBER)) # фильтр с типом апдейта
async def user_unblocked_bot(event: ChatMemberUpdated):
    print(f"Пользователь {event.from_user.id} - {event.from_user.full_name} разблокировал бота")

# help
@dp.message(my_help_filter)
async def process_help(message: Message):
    await message.answer("Команды:\n/start - Старт \n/help - О боте\n/dog - фотка собаки!\n/breeds - породы ")



@dp.message(Command(commands=['dog']))
async def answer_dog(message: Message, command: CommandObject):
    if command.args:
        s = requests.get(f"https://dog.ceo/api/breed/{command.args}/images/random")
    else:
        s = requests.get(f"https://dog.ceo/api/breeds/image/random")
    json_s = s.json()
    if json_s.get("status")== "success":
        print(json_s.get("message"))
        await message.answer_photo(photo=json_s.get("message"))
    else:
        await message.answer("ТЫ не прав не могу так")
    print(s.content)



# @dp.message(Command(commands=["breeds"]))
# async def show_breeds(message: Message):
#     result = requests.get("https://dog.ceo/api/breeds/list/all")
#     result_json = result.json()
#     dogs_types = result_json["message"].keys()
#     s = "\n".join(list(dogs_types)[:30]) #сделать 30 собак и сделать вывод столбиком
#     await message.answer(s)

# @dp.message(count_message)
# async def process_80_chr(message: Message):
#     await message.answer(str(len(message.text)))
#
# @dp.message()
# async def handle_message(message: Message):
#     if not message.text:
#         await message.answer("Это не прошло фильтры")
#         return
#     if len(message.text) < 20:
#         await message.answer("Коротко и ясно!")
#     else:
#         await message.answer("Много букв, но я осилил!")

VIP={}
@dp.message(Command(commands=["secret"]),F.from_user.id.in_(VIP))
async def  process_secret(message: Message):
    await message.answer("Добро пожаловать")


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

