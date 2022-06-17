import random
from Bot import innexia, CMD_HNDLR as hndlr
from telethon import events, Button
from telethon.tl.custom import button
from time import time
from datetime import datetime
from assets.pics import PHOTO
from Bot.plugins import *

HELP_PIC = f"{random.choice(PHOTO)}"



  
           
@innexia.on(events.NewMessage(pattern="/help"))           
@innexia.on(events.CallbackQuery(pattern=r"help_back"))
async def helpback(event):
      await event.edit(
            HELP_TXT,
            buttons=[
            [
            Button.inline("ᴀᴅᴍɪɴ", data="admin"),
            Button.inline("ᴀғᴋ", data="afk"),
            Button.inline("ᴄʜᴀᴛʙᴏᴛ", data="chatbot"),
           ],
           [
            Button.inline("ʙᴀᴄᴋ", data="home"),
           ],
           ], 
           )         
           
# From here                      
@innexia.on(events.CallbackQuery(pattern=r"admin"))
async def help_admin(event):
       await event.edit(
            ADMIN_TXT,
            buttons=[
                [
            Button.inline("ʙᴀᴄᴋ", data="help_back"),
            Button.inline("ᴄʟᴏsᴇ", data="close"), 
            ],
            ],
            ) 
                 
                                                       
@innexia.on(events.CallbackQuery(pattern=r"afk"))
async def help_afk(event):
       await event.edit(
            AFK_TXT,
            buttons=[
                [
            Button.inline("ʙᴀᴄᴋ", data="help_back"),
            Button.inline("ᴄʟᴏsᴇ", data="close"), 
            ],
            ],
            ) 
                 
@innexia.on(events.CallbackQuery(pattern=r"chatbot"))
async def help_carbon(event):
       await event.edit(
           CHATBOT_TXT,
            buttons=[
                [
            Button.inline("ʙᴀᴄᴋ", data="help_back"),
            Button.inline("ᴄʟᴏsᴇ", data="close"), 
            ],
            ],
            ) 

@innexia.on(events.CallbackQuery(pattern=r"close"))
async def help_connect(event):
       await event.delete() 
