import logging
import json
from random import random
import secrets
import time
from pyrogram import filters
from WebStreamer.utils.streaamapi import wait_time
from WebStreamer.vars import Var
from urllib.parse import quote_plus
from WebStreamer.bot import StreamBot, waiting
from WebStreamer.utils import get_hash, get_name, user_in_streaam, humanbytes
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserNotParticipant
import traceback
import asyncio
import aiohttp
import string



@StreamBot.on_message(
    filters.private
    & (
        filters.document
        | filters.video
        | filters.animation
        | filters.photo
    ),
    group=4,
)
async def media_receive_handler(c, m: Message):
    if not await user_in_streaam(m.chat.id):
        await m.reply_text(
            text="<b>👋🏻 Hello, Sorry User This Bot Only Made For Streaam.net users To Upload Their Files easily.</b>\n\n<b>🔅If We Did Any Mistake or You Are User Of Streaam.net Kindly Contact Admins.</b>\n\n<b>⚠️@SID12O</b>\n<b>⚠️@Hcktech</b>\n<b>⚠️@LegendAkshay</b>"
        )
        return
    if wait_time(m.chat.id):
        print('------------------------')
        await m.reply_text(
            text="**🔅Please Wait For The First 2 File To Upload Successfully, After That Send Me Another Files.**",
            quote=True
        )
        return
    else:
        edit_msg=await m.reply_text(
            text='wait',
            quote=True
        )
        if waiting[m.chat.id] >= 3:
            await edit_msg.edit_text(
                text="Please wait until a upload is completed"
            )
            while not waiting[m.chat.id] <= 2:
                await asyncio.sleep(1)
            print(f'wait to uploading {m.chat.id} - {waiting[m.chat.id]}')
        log_msg = await m.forward(chat_id=Var.BIN_CHANNEL)
        stream_link = f"{Var.URL}{log_msg.message_id}/{quote_plus(get_name(m))}?hash={get_hash(log_msg)}"
        short_link = f"{Var.URL}{get_hash(log_msg)}{log_msg.message_id}"
        await log_msg.reply_text(text=f"Requested by [{m.from_user.first_name}](tg://user?id={m.from_user.id})\nlink : {stream_link}\n**User ID:** `{m.from_user.id}`", disable_web_page_preview=True, parse_mode="Markdown", quote=True)
        # -------------------------------------
        alphabet = string.ascii_lowercase + string.digits
        # randomhash=''.join(secrets.choice(alphabet) for _ in range(8))
        randomhash= f"{log_msg.message_id}"
        url='https://streaam.net/api/addremote.php'
        data1={
            'uid': m.chat.id,
            'url': stream_link,
            "hash": randomhash
        }
        await edit_msg.edit_text(
            text="**Uploading To Your Streaam.net Account.....**"
        )
        async with aiohttp.ClientSession() as session:
            async with session.get(url, params=data1) as resp:
                resp=await resp.json()
                edt_text=str(resp['result'])
                print('1: ', edt_text)
                await edit_msg.edit_text(
                    text=edt_text
                )
        # ---------------------------------------
        sleep_time = 3
        url='https://streaam.net/api/checkremote.php'
        data={
            'uid': m.chat.id,
            "hash": randomhash
        }
        
        resp = '{"finished":false}'
        resp = json.loads(resp)
        #resp={"finished": False}
        #while not resp['finished']:
        print(randomhash)
        seconds = time.time()
        while True:
            await asyncio.sleep(sleep_time)
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.get(url, params=data) as resp:
                        resp=await resp.json()
                        if resp['finished']:
                            edt_text=f"**🔥Uploaded Successfully In Your Streaam Account Here is Your Link :** {str(resp['url'])}\n\n**💥Uploaded To Your Streaam Account**: {m.chat.id}\n**🔅Join Official Channel For Latest Updates @streaam_Net**"
                            # print(edt_text)
                            await edit_msg.edit_text(
                                text=edt_text
                            )
                            break
                        # print(resp)
                        if resp['files'][0]['status'] == "waiting":
                            await edit_msg.edit_text(
                            text=f"Server is Slow,Contact Admins To fix it |{int(time.time() - seconds)}"
                            )
                        else:
                            downloaded=humanbytes(resp['files'][0]['downloaded'])
                            size=humanbytes(resp['files'][0]['size'])
                            edt_text=f"**♻️Uploading.....**\n{downloaded} / {size}\nSec = {int(time.time() - seconds)}"
                            # print(edt_text)
                            await edit_msg.edit_text(
                                text=edt_text
                            )
            except TimeoutError:
                print("Couldn't connect to the site URL..!")
            except Exception:
                traceback.print_exc()
    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=data) as resp:
            resp=await resp.json()
            print(resp)
    waiting[m.chat.id] = waiting[m.chat.id] - 1
@StreamBot.on_message(filters.command('stat') & filters.user(Var.ADMIN))
async def stat(_, m):
    print(waiting)
    await m.reply_text(
        text=waiting
    )
