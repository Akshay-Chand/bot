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

@StreamBot.on_message(filters.command(["restart", "restarts"]))
async def restart_bot(message):
    await message.reply("Bot will be restarted...")
    fuck = [sys.executable, "-m", "WebStreamer"]
    os.execl(sys.executable, fuck)
