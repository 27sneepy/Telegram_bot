from environs import Env

env = Env() # настройки
env.read_env() # где файл .env и получение всех переменных из него

BOT_TOKEN = env('BOT_TOKEN')