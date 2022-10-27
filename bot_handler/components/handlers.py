from aiogram import Dispatcher, types
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardRemove
from components.api_connector import UserAdd, GetCommandsList

async def CommandStart(message: types.Message):
    await UserAdd(
        str(message.bot.id),
        str(message.from_user.id),
        message.from_user.username,
        message.from_user.first_name,
        message.from_user.last_name
    )
    try:
        start_cmd = GetCommandsList(str(message.bot.id))['start']
        answer_text = start_cmd['text']
    except: answer_text = "Для бота не создана команда start"
    await message.answer(answer_text, reply_markup = ReplyKeyboardRemove())

async def CommandReact(message: types.Message):
    await message.answer("Привет!", reply_markup = ReplyKeyboardRemove())

async def CommandBotID(message: types.Message):
    await message.answer(str(message.bot.id), reply_markup = ReplyKeyboardRemove())

async def MessageReact(message: types.Message):
    await message.answer(message.text, reply_markup = ReplyKeyboardRemove())

def register_message_handlers(dp:Dispatcher, bot_id: str):
    bot_commands = GetCommandsList(bot_id).keys()
    dp.register_message_handler(CommandStart, commands = ['start'])
    dp.register_message_handler(CommandBotID, commands = ['you'])
    dp.register_message_handler(CommandReact, commands = bot_commands)
    dp.register_message_handler(MessageReact, Text(equals=['Привет']))
