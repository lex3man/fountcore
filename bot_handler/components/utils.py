from components.api_connector import GetKeybordConfig
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

async def MakeStdKeyboard(keyboardName: str):
    config = await GetKeybordConfig(keyboardName)
    keyboard = ReplyKeyboardMarkup(resize_keyboard = True)
    for row in range(10):
        cp = 0
        for btn in config.keys():
            if int(config[btn]['row']) == row:
                cp += 1
                if cp == 1: keyboard.add(KeyboardButton(btn))
                else: keyboard.insert(KeyboardButton(btn))
    return keyboard
