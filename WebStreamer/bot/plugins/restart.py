import asyncio
import io
import logging
import os
import shutil
import sys
import time
import traceback

from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from WebStreamer.bot import StreamBot
from WebStreamer.vars import Var
from WebStreamer.__main__ import * # yea 
from logging.handlers import RotatingFileHandler

@StreamBot.on_message(filters.command(["restart"]))
async def restart(bot, message,*args):
    await message.reply_text(text="<b>Bot Restarting.... </b>") 
    args = [sys.executable, "-m", "WebStreamer"]
    os.execl(sys.executable,*args)
