import random
from Bot import innexia, hndlr
from telethon import events, Button
from telethon.tl.custom import button
from time import time
from datetime import datetime
from assets.pics import PHOTO
from assets.string import *

HELP_PIC = f"{random.choice(PHOTO)}"


@innexia.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hndlr))
async def help(event):
       await event.client.send_file(event.chat_id,
                                  HELP_PIC,
                                  caption=HELP_TXT,
                                  buttons=[
           [
            Button.inline("ᴀᴅᴍɪɴ", data="admin"),
            Button.inline("ᴀғᴋ", data="afk"),
            Button.inline("ᴄᴀʀʙᴏɴ", data="carbon"),
           ],
           [
            Button.inline("ᴄᴏɴɴᴇᴄᴛ", data="connect"),
            Button.inline("ғɪʟᴛᴇʀ", data="filter"),
            Button.inline("ɢʀᴏᴜᴘ", data="group"),
           ],
           [
            Button.inline("ʟᴏᴄᴋs", data="locks"),
            Button.inline("ᴍᴜsɪᴄ", data="music"), 
            Button.inline("ɴᴏᴛᴇs", data="notes"), 
           ],
           [
            Button.inline("ʀᴜʟᴇs", data="rules"),           
            Button.inline("sᴛɪᴄᴋᴇʀs", data="stickers"),
            Button.inline("ᴛᴏᴏʟs", data="tools"),
           ], 
           [
            Button.inline("ᴜsᴇʀ", data="user"),
            Button.inline("ᴡᴇʟᴄᴏᴍᴇ", data="welcome"),
           ], 
           [
            Button.inline("ʙᴀᴄᴋ", data="home"),
           ],
           ], 
           )              

  
  

           
           
@innexia.on(events.CallbackQuery(pattern=r"help_back"))
async def helpback(event):
      await event.edit(
            Mig_Help,
            buttons=[
           [
            Button.inline("ᴀᴅᴍɪɴ", data="admin"),
            Button.inline("ᴀғᴋ", data="afk"),
            Button.inline("ᴄᴀʀʙᴏɴ", data="carbon"),
           ],
           [
            Button.inline("ᴄᴏɴɴᴇᴄᴛ", data="connect"),
            Button.inline("ғɪʟᴛᴇʀ", data="filter"),
            Button.inline("ɢʀᴏᴜᴘ", data="group"),
           ],
           [
            Button.inline("ʟᴏᴄᴋs", data="locks"),
            Button.inline("ᴍᴜsɪᴄ", data="music"), 
            Button.inline("ɴᴏᴛᴇs", data="notes"), 
           ],
           [
            Button.inline("ʀᴜʟᴇs", data="rules"),           
            Button.inline("sᴛɪᴄᴋᴇʀs", data="stickers"),
            Button.inline("ᴛᴏᴏʟs", data="tools"),
           ], 
           [
            Button.inline("ᴜsᴇʀ", data="user"),
            Button.inline("ᴡᴇʟᴄᴏᴍᴇ", data="welcome"),
           ], 
           [
            Button.inline("ʙᴀᴄᴋ", data="home"),
           ],
           ], 
           )         
           
From here                      
@innexia.on(events.CallbackQuery(pattern=r"admin"))
async def help_admin(event):
       await event.edit(
            ADMIN_TXT,
            buttons=[
                [
            Button.inline("ʙᴀᴄᴋ", data="help_back"),
            Button.inline("ᴄʟᴏsᴇ, data="close"), 
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
            Button.inline("ᴄʟᴏsᴇ, data="close"), 
            ],
            ],
            ) 
                 
@innexia.on(events.CallbackQuery(pattern=r"carbon"))
async def help_carbon(event):
       await event.edit(
            CARBON_TXT,
            buttons=[
                [
            Button.inline("ʙᴀᴄᴋ", data="help_back"),
            Button.inline("ᴄʟᴏsᴇ, data="close"), 
            ],
            ],
            ) 

@innexia.on(events.CallbackQuery(pattern=r"connect"))
async def help_connect(event):
       await event.edit(
            CONNECT_TXT,
            buttons=[
                [
            Button.inline("ʙᴀᴄᴋ", data="help_back"),
            Button.inline("ᴄʟᴏsᴇ, data="close"), 
            ],
            ],
            ) 
                 
@innexia.on(events.CallbackQuery(pattern=r"filter"))
async def help_filter(event):
       await event.edit(
            FILTER_TXT,
            buttons=[
                [
            Button.inline("ʙᴀᴄᴋ", data="help_back"),
            Button.inline("ᴄʟᴏsᴇ, data="close"), 
            ],
            ],
            ) 

@innexia.on(events.CallbackQuery(pattern=r"group"))
async def help_group(event):
       await event.edit(
            GROUP_TXT,
            buttons=[
                [
            Button.inline("ʙᴀᴄᴋ", data="help_back"),
            Button.inline("ᴄʟᴏsᴇ, data="close"), 
            ],
            ],
            ) 

@innexia.on(events.CallbackQuery(pattern=r"locks"))
async def help_locks(event):
       await event.edit(
            LOCK_TXT,
            buttons=[
                [
            Button.inline("ʙᴀᴄᴋ", data="help_back"),
            Button.inline("ᴄʟᴏsᴇ, data="close"), 
            ],
            ],
            ) 
                 
@innexia.on(events.CallbackQuery(pattern=r"music"))
async def help_music(event):
       await event.edit(
            MUSIC_TXT,
            buttons=[
                [
            Button.inline("ʙᴀᴄᴋ", data="help_back"),
            Button.inline("ᴄʟᴏsᴇ, data="close"), 
            ],
            ],
            ) 
@innexia.on(events.CallbackQuery(pattern=r"notes"))
async def help_notes(event):
       await event.edit(
            NOTE_TXT,
            buttons=[
                [
            Button.inline("ʙᴀᴄᴋ", data="help_back"),
            Button.inline("ᴄʟᴏsᴇ, data="close"), 
            ],
            ],
            ) 
                 
                                                       
@innexia.on(events.CallbackQuery(pattern=r"rules"))
async def help_rules(event):
       await event.edit(
            RULE_TXT,
            buttons=[
                [
            Button.inline("ʙᴀᴄᴋ", data="help_back"),
            Button.inline("ᴄʟᴏsᴇ, data="close"), 
            ],
            ],
            ) 

@innexia.on(events.CallbackQuery(pattern=r"stickers"))
async def help_stickers(event):
       await event.edit(
            STCKR_TXT,
            buttons=[
                [
            Button.inline("ʙᴀᴄᴋ", data="help_back"),
            Button.inline("ᴄʟᴏsᴇ, data="close"), 
            ],
            ],
            ) 
                 
@innexia.on(events.CallbackQuery(pattern=r"tools"))
async def help_tools(event):
       await event.edit(
            TOOL_TXT,
            buttons=[
                [
            Button.inline("ʙᴀᴄᴋ", data="help_back"),
            Button.inline("ᴄʟᴏsᴇ, data="close"), 
            ],
            ],
            ) 
                 
@innexia.on(events.CallbackQuery(pattern=r"user"))
async def help_user(event):
       await event.edit(
            USER_TXT,
            buttons=[
                [
            Button.inline("ʙᴀᴄᴋ", data="help_back"),
            Button.inline("ᴄʟᴏsᴇ, data="close"), 
            ],
            ],
            ) 
                 
                                                       
@innexia.on(events.CallbackQuery(pattern=r"welcome"))
async def help_welcome(event):
       await event.edit(
            WELCOME_TXT,
            buttons=[
                [
            Button.inline("ʙᴀᴄᴋ", data="help_back"),
            Button.inline("ᴄʟᴏsᴇ, data="close"), 
            ],
            ],
            ) 
                 
                                                       
                                                       
                                                       
                                                                        

                 
                                                       
                                                       
                 
                                                       
                 
                                                       
                                                       
                                                       
                                                       
