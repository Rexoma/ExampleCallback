import os

HELP_TXT = """
π·π΄π {mention}
π·π΄ππ΄ πΈπ πΌπ π·π΄π»πΏ πΌπ΄π½π π΅πΎπ ππΎπ:
"""

ADMIN_TXT = """
β Some people need to be publicly banned; spammers, annoyances, or just trolls.
Make it easy to promote and demote users with the admin module!
β£ /tban - Ban A User For Specific Time
β£ /warn - Warn A User
β£ /dwarn - Delete the replied message warning its sender
β£ /rmwarns - Remove All Warning of A User
β£ /warns - Show Warning Of A User
β£ /promote - Promote A Member
β£ /fullpromote - Promote A Member With All Rights
β£ /demote - Demote A Member
β£ /tmute - Mute A User For Specific Time
β£ /ban_ghosts - Ban Deleted Accounts
β£ /report | @admins | @admin - Report A Message To Admins.
β₯ you promote or demote an admin manually, 
and Innexia doesn't realise it immediately. This is because 
to avoid spamming telegram servers, admin status is cached locally.
""" 

AFK_TXT = """
β Enables afk for your account
βdescription: When you are in afk if any one tags you then your bot will reply as he is offline.
βAFK mean away from keyboard.
options: If you want AFK reason with reason.
β£ usage: /afk <reason>
β£ examples: /afk Let Me Sleep.
β£ note: "Switches off AFK when you type back anything, anywhere. You can use #afk in message to continue in afk without breaking it.
"""

ANTICHANNEL_TXT = """
your groups to stop anonymous channels sending messages into your chats.
*Type of messages*
β£ document
β£ photo
β£ sticker
β£ animation
β£ video
β£ text
β Admin Commands
β£ /antichannel [on / off] - Anti- channel  function 
β₯Note: If linked_channel  send any containing characters in this type when on  function no del.
""" 

BAN_TXT = """
β Some people need to be publicly banned; spammers, annoyances, or just trolls.

β£ ?kickme - To self Kick you from a chat.
β£ ?kick - To kick someone from a chat.
β£ ?unban - To unban a member from the chat.
β£ ?ban - To Ban Someone from a chat.
β£ ?dban - To delete the replied msg and bans the user.
β£ ?sban - To delete the replied msg and kicks the user.
β£ ?skick - To Delete Your msg and kicks the user 
β£ ?dkick - To delete your msg and and kicks the replied user.
"""
CLEANER_TXT = """
β This is A Module To Remove Deleted Accounts From Your Groups!

β£ /zombies - To find zombies accounts in your chat.
β£ /zombies clean - To remove the deleted accounts from your chat.
"""

EXTRA_TXT = """
"""
