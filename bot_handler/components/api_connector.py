import requests, aiohttp, os

server_host = os.environ.get("CORE_HOST")
if os.environ.get("SSL") == 'False': server_url = f'http://{server_host}:{os.environ.get("PORT")}/'
else: server_url = f'https://{server_host}/'

async def GetContent(bot_id: str, request_text: str):
    url = server_url + 'bots/content/'
    async with aiohttp.ClientSession() as session:
        async with session.get(url, params={'bid':bot_id, 'data':request_text}) as resp:
            response = await resp.json()
            return response

async def UserAdd(bot_id: str, user_id: str, username: str = '', first_name: str = '', last_name: str = ''):
    data = {
        'bid':bot_id,
        'tid':user_id,
        'username':username,
        'fname':first_name,
        'lname':last_name,
    }
    url = server_url + 'users/new/'
    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=data) as resp:
            response = await resp.json()
            return response

def BotStartReg(bot_id: str, bot_token: str):
    url = server_url + 'bots/logging/'
    data = {'bid':bot_id, 'token':bot_token}
    response = requests.post(url, json=data)
    return response.json()

def GetCommandsList(bot_id: str):
    url = server_url + 'bots/commands/'
    data = {'bid':bot_id}
    response = requests.get(url, params=data)
    return response.json()

async def GetKeybordConfig(keyboardName: str):
    url = server_url + 'bots/keyb/'
    async with aiohttp.ClientSession() as session:
        async with session.get(url, params={'kb':keyboardName}) as resp:
            response = await resp.json()
            return response

