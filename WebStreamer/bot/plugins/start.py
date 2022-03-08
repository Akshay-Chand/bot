# This file is a part of TG-FileStreamBot
# Coding : Jyothis Jayanth [@EverythingSuckz]

from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from WebStreamer.bot import StreamBot
from WebStreamer.vars import Var
from WebStreamer.utils import user_in_streaam


@StreamBot.on_message(filters.command(["start", "help"]))
async def unauth(_, m: Message):
  if await user_in_streaam(m.chat.id):
    await m.reply_text(
          f'**Hi {m.from_user.mention(style="md")},\nSend or Forward Me File in .Mp4 or .Mkv Format To Upload in Your Streaam.net Account.**'
      )
  else:
    await m.reply_text(
        text="<b>👋🏻 Hello, Sorry User This Bot Only Made For Streaam.net users To Upload Their Files easily.</b>\n\n<b>🔅If We Did Any Mistake or You Are User Of Streaam.net Kindly Contact Admins.</b>\n\n<b>⚠️@SID12O</b>\n<b>⚠️@Hcktech</b>\n<b>⚠️@LegendAkshay</b>"
    )
