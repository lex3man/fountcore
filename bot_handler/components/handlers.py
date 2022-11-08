from aiogram import Dispatcher, types
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardRemove
from components.api_connector import UserAdd, GetCommandsList
from components.utils import MakeStdKeyboard

async def CommandStart(message: types.Message):
    await UserAdd(
        str(message.bot.id),
        str(message.from_user.id),
        message.from_user.username,
        message.from_user.first_name,
        message.from_user.last_name
    )
    keyboard = ReplyKeyboardRemove()
    try:
        start_cmd = GetCommandsList(str(message.bot.id))['start']
        answerText = start_cmd['text']
        if start_cmd['keyboard'] != 'None': keyboard = await MakeStdKeyboard(start_cmd['keyboard'])
    except: answerText = "Для бота не создана команда start"
    await message.answer(answerText, reply_markup = keyboard)

async def CommandReact(message: types.Message):
    keyboard = ReplyKeyboardRemove()
    cmd = GetCommandsList(str(message.bot.id)).get(message.text.replace('/',''), {})
    answerText = cmd.get('text', 'Не на всё подряд я отвечаю')
    if cmd['keyboard'] != 'None': keyboard = await MakeStdKeyboard((cmd['keyboard']))
    await message.answer(answerText, reply_markup = keyboard) 

async def CommandBotID(message: types.Message):
    keyboard = ReplyKeyboardRemove()
    await message.answer(str(message.bot.id), reply_markup = keyboard)

async def MessageReact(message: types.Message):
    keyboard = ReplyKeyboardRemove()
    await message.answer(message.text, reply_markup = keyboard)

def register_message_handlers(dp:Dispatcher, bot_id: str):
    bot_commands = GetCommandsList(bot_id).keys()
    dp.register_message_handler(CommandStart, commands = ['start'])
    dp.register_message_handler(CommandBotID, commands = ['you'])
    dp.register_message_handler(CommandReact, commands = bot_commands)
    dp.register_message_handler(MessageReact, Text(equals=['Привет']))
