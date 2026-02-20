from http.client import responses
from config import Config, load_config
import requests
from bs4 import BeautifulSoup

config: Config = load_config(".env")
bot_token=config.bot.token


# GET - на получение данных с сервера - html / json
# POST - отправляем данные на сервер или сохраняем

# response=requests.get("https://google.com")
# print(response.text)

# 200 - выполнено 201
# 404 500 412
# s=requests.get(f"https://api.telegram.org/bot{bot_token}/getMe")
# print(s.text)
# JSON

# urls = ['https://google.com','https://rutube.ru','https://vk.com']
# pages={}
# for url in urls:
#     response = requests.get(url)
#     html=response.text
#     soup = BeautifulSoup(response.text, 'html.parser')
#     page_title = soup.title.string if soup.title else "NO TITLE"
#     pages[page_title]=html
# print(pages)



