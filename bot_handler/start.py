from sys import argv
from aiogram import Bot, executor
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from components.handlers import register_message_handlers
from components.api_connector import BotStartReg

bot_token = argv[1]
bot_id = None

def on_startup(dp):
    register_message_handlers(dp, bot_id=str(bot_id))

def BotDp(token):
    global bot_id
    bot = Bot(token)
    bot_id = bot.id
    dp = Dispatcher(bot, storage = MemoryStorage())
    dp.middleware.setup(LoggingMiddleware())
    BotStartReg(str(bot.id), token)
    return dp

dp = BotDp(bot_token)

executor.start_polling(dp, skip_updates = True, on_startup = on_startup(dp))
