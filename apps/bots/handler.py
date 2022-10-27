from .models import Bot, Button, Keyboard, ContentBlock, State
from apps.users.models import User, TelegramAsset

class Bot_reaction:
    
    def __init__(self, botID: str, userID: str):
        self.bot = Bot.objects.get(bot_id = botID)
        self.assets = TelegramAsset.objects.get(tid = userID)
        self.user = User.objects.get(telegram = self.assets)
    
    def FeelAction(self, text: str):
        pass