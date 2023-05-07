import logging
from aiogram import executor
from bot.handler import *
from bot.dispacher import dp


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)
