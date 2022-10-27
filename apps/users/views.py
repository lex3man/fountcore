from string import digits
from django.http import JsonResponse
from django.views import View
from .models import User, TelegramAsset
from apps.bots.models import Bot
import json, random

def uid_gen():
    while True:
        number = ''.join(random.choice('0123456789ABCDEF') for x in range(6))
        try: User.objects.get(uid = number)
        except User.DoesNotExist: break
    return number

class UserAdd(View):
    def post(self, request):
        usr_data = json.loads(request.body)
        try:
            TelegramAsset.objects.get(tid = usr_data['tid'])
            resp = {
                'status':'error',
                'msg':'already exist'
            }
        except TelegramAsset.DoesNotExist:
            bot = Bot.objects.get(bot_id = usr_data['bid'])
            TAsset = TelegramAsset(
                tid = usr_data['tid'],
                username = usr_data['username'],
                fname = usr_data['fname'],
                lname = usr_data['lname'],
                on_fox = True,
                from_bot = bot
            )
            TAsset.save()
            UserSet = User(
                uid = uid_gen(),
                name = TAsset.fname,
                telegram = TAsset,
                status = 'usr'
            )
            UserSet.save()

            resp = {
                "status":"OK",
                "msg":f"User {usr_data['fname']} with ID{usr_data['tid']} registerd"
            }
        
        return JsonResponse(resp)