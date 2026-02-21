from dataclasses import dataclass
from environs import Env
# from os import getenv
@dataclass
class TgBot:
    token: str

@dataclass
class Config:
    bot: TgBot


def load_config(path=None) -> Config:
        env = Env()
        env.read_env(path)
        return Config(
            bot=TgBot(token=env.str("BOT_TOKEN"))
        )
