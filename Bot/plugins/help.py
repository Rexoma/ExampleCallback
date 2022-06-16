from Bot import innexia, hndlr
from telethon import events, Button
from telethon.tl.custom import button
from time import time
from datetime import datetime
  


@innexia.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hndlr))
async def help(event):
    if event.sender_id in SUDO_USERS:
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
            Button.inline("ʙᴀᴄᴋ", data="ʙᴀᴄᴋ"),
           ],
           ], 
           )              

  
  

           
           
@Mig10.on(events.CallbackQuery(pattern=r"help_back"))
async def helpback(event):
   if event.query.user_id in SUDO_USERS:    
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
            Button.inline("ʙᴀᴄᴋ", data="ʙᴀᴄᴋ"),
           ],
           ], 
           )         
           
From here                      
@Mig10.on(events.CallbackQuery(pattern=r"spam"))
async def help_spam(event):
   if event.query.user_id in SUDO_USERS:    
       await event.edit(
            spam_msg,
            buttons=[
                [
            Button.inline("< Back", data="help_back"),
            ],
            ],
            ) 
   else:
        Alert = (
                "Noob !! Make Your Own Mighty X Spam Bots !! @MightyXSpam"
            )
        await event.answer(Alert, cache_time=0, alert=True)
                 
                                                       
@Mig10.on(events.CallbackQuery(pattern=r"raid"))
async def help_raid(event):
     if event.query.user_id in SUDO_USERS:
        await event.edit(
            raid_msg,
            buttons=[
            [
            Button.inline("< Back", data="help_back"),
            ],
            ],
            )  
     else:
        Alert = (
                "Noob !! Make Your Own Mighty X Spam Bots !! @MightyXSpam"
            )
        await event.answer(Alert, cache_time=0, alert=True)
       


@Mig10.on(events.CallbackQuery(pattern=r"extra"))
async def help_extra(event):
   if event.query.user_id in SUDO_USERS:
        await event.edit(
            extra_msg,
            buttons=[
            [
            Button.inline("< Back", data="help_back"),                        
            ],
            ],
            )
   else:
        Alert = (
                "Noob !! Make Your Own Mighty X Spam Bots !! @MightyXSpam"
            )
        await event.answer(Alert, cache_time=0, alert=True)
