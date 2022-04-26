from pyrogram import Client
from pyrogram.types import Message
import traceback
import asyncio
import aiohttp
from WebStreamer.bot import StreamBot, waiting

async def user_in_streaam(id: int):
    async with aiohttp.ClientSession() as session:
        url = f'https://streaam.net/dash/check.php'
        params = {'id': id}

        async with session.get(url, params=params) as resp:
            text_resp = await resp.text()
            if text_resp == 'ok':
                return True
            else:
                return False

def wait_time(chat_id: int):
    if not chat_id in waiting:
        waiting[chat_id] = 1
        print('create dic ', waiting[chat_id])
        return False
    else:
        if waiting[chat_id] >= 2:
            print(f'wait {chat_id} - {waiting[chat_id]}')
            return True
        else:
            waiting[chat_id] = waiting[chat_id] + 1
            print(f'cont- {waiting[chat_id]}')
            return False
