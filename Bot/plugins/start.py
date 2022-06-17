import asyncio
import os
import random
from telethon.tl.functions.users import GetFullUserRequest
from telethon import events, Button
from telethon.tl.custom import button
from Bot import innexia, OWNER_ID
from Bot.help import *
from assets.pics import PHOTO

START_IMG = f"{random.choice(PHOTO)}"

start_button = [
        ]
        Button.url("ᴀᴅᴅ ᴍᴇ ᴛᴏ ɢʀᴏᴜᴘ", "https://t.me/rexomasupport"),
        ], 
        [
        Button.url("sᴜᴘᴘᴏʀᴛ", "https://t.me/rexomasupport"), 
        Button.url("ᴜᴘᴅᴀᴛᴇs", "https://t.me/rexomaupdate")
        ],
        [
        Button.inline("ʜᴇʟᴘ ᴍᴇ", data="help_back"), 
        Button.inline("ᴀʙᴏᴜᴛ ᴍᴇ", data="innexia_about") 
        ], 
]
               
               
        
#USERS 


@innexia.on(events.NewMessage(pattern="/start"))
async def start(event):              
    if event.is_private:
       InnexiaBot = await event.client.get_me()
       bot_name = InnexiaBot.first_name
       bot_id = InnexiaBot.id
       replied_user = await event.client(GetFullUserRequest(event.sender_id))
       chatid = event.chat_id
       firstname = replied_user.user.first_name
       userid = replied_user.user.id
       ownermsg = f"𝙷𝙴𝙻𝙻𝙾 𝙱𝚘𝚜𝚜 [{firstname}](tg://user?id={userid}),\n𝙼𝚈 𝙽𝙰𝙼𝙴 𝙸𝚂 [{bot_name}](tg://user?id={bot_id}), 𝙰 𝙿𝙾𝚆𝙴𝚁𝙵𝚄𝙻 𝚂𝙼𝙰𝚁𝚃 𝙶𝚁𝙾𝚄𝙿 𝚁𝙾𝙱𝙾𝚃\n𝚆𝙸𝚃𝙷 𝙼𝙰𝙽𝚈 𝙰𝙼𝙰𝚉𝙸𝙽𝙶 𝙵𝙴𝙰𝚃𝚄𝚁𝙴𝚂. 𝙸 𝙲𝙰𝙽 𝙷𝙴𝙻𝙿 𝚈𝙾𝚄 𝚃𝙾 𝙼𝙰𝙽𝙰𝙶𝙴 𝚈𝙾𝚄𝚁 𝙶𝚁𝙾𝚄𝙿𝚂,\n𝙹𝚄𝚂𝚃 𝙰𝙳𝙳 𝙼𝙴 𝚃𝙾 𝚈𝙾𝚄𝚁 𝙶𝚁𝙾𝚄𝙿 𝙰𝙽𝙳 𝙴𝙽𝙹𝙾𝚈"
       usermsg = f"𝙷𝙴𝙻𝙻𝙾 [{firstname}](tg://user?id={userid}),\n𝙼𝚈 𝙽𝙰𝙼𝙴 𝙸𝚂 [{bot_name}](tg://user?id={bot_id}), 𝙰 𝙿𝙾𝚆𝙴𝚁𝙵𝚄𝙻 𝚂𝙼𝙰𝚁𝚃 𝙶𝚁𝙾𝚄𝙿 𝚁𝙾𝙱𝙾𝚃\n𝚆𝙸𝚃𝙷 𝙼𝙰𝙽𝚈 𝙰𝙼𝙰𝚉𝙸𝙽𝙶 𝙵𝙴𝙰𝚃𝚄𝚁𝙴𝚂. 𝙸 𝙲𝙰𝙽 𝙷𝙴𝙻𝙿 𝚈𝙾𝚄 𝚃𝙾 𝙼𝙰𝙽𝙰𝙶𝙴 𝚈𝙾𝚄𝚁 𝙶𝚁𝙾𝚄𝙿𝚂,\n𝙹𝚄𝚂𝚃 𝙰𝙳𝙳 𝙼𝙴 𝚃𝙾 𝚈𝙾𝚄𝚁 𝙶𝚁𝙾𝚄𝙿 𝙰𝙽𝙳 𝙴𝙽𝙹𝙾𝚈"
       if event.sender_id == OWNER_ID:
            await event.client.send_file(chatid,
                  START_IMG,
                  caption=ownermsg, 
                  buttons=start_button)
       else:
            await event.client.send_file(chatid,
                  START_IMG,
                  caption=usermsg, 
                  buttons=start_button)
