import json

from apps.users.models import TelegramAsset
from .models import Bot, Button, Keyboard, ContentBlock, State, Log, Command
from django.http import JsonResponse
from django.views import View

class GetToken(View):
    def get(self, request):
        bot_name = request.GET.get('bot')
        try:
            bot_conf = Bot.objects.get(caption = bot_name)
            return JsonResponse({'token':bot_conf.token})
        except: return JsonResponse({'error':'no such bot'})

class GetBotInfo(View):
    def get(self, request):
        bid = request.Get.get('id')
        try:
            bot = Bot.objects.get(bot_id = bid)
            return JsonResponse({
                'Bot_name':bot.caption,
                'Bot_type':bot.bot_type,
                'Description':bot.description,
                'Status':bot.active
            })
        except: return JsonResponse({'error':'bad ID'})

class StartReg(View):
    def post(self, request):
        data = json.loads(request.body)
        init_bot = Bot.objects.get(token = data['token'])
        log = Log(bot = init_bot, event_type = 'start', details = '')
        log.save()
        try: Bot.objects.get(bot_id = data['bid'])
        except Bot.DoesNotExist: 
            init_bot.bot_id = data['bid']
            init_bot.save()
            log = Log(bot = init_bot, event_type = 'update', details = f"new id {data['bid']}")
            log.save()
        return JsonResponse({"status":"OK"})

class GetCommands(View):
    def get(self, request):
        init_bot = Bot.objects.get(bot_id = request.GET.get('bid'))
        data = {}
        for cmd in Command.objects.filter(bot = init_bot):
            if cmd.keyboard == None: kb = "None"
            else: kb = cmd.keyboard.caption
            if cmd.next_block == None: nb = "None"
            else: nb = cmd.next_block.caption
            data.update({
                cmd.keyword:{
                    'text':cmd.answer,
                    'keyboard':kb,
                    'next':nb
                }
            })
        return JsonResponse(data)

class FindAnswer(View):
    def get(self, request):
        bid = request.GET.get('bid')
        tuid = request.GET.get('tid')
        text = request.GET.get('text')
        try:
            tuser = TelegramAsset.objects.get(tid = tuid)
            userCurrentState = State.objects.get(sid = tuser.state_id)
            requestBot = Bot.objects.get(bot_id = bid)
            contentBlock = ContentBlock.objects.filter(bot = requestBot).filter(state = userCurrentState).get(content = text)
            data = {
                'status':'OK',
                'content':{
                    'caption':contentBlock.caption,
                    'text':contentBlock.content,
                }
            }
        except: data = {"status":"error", "msg":"some of objects not found"}
        return JsonResponse(data)
