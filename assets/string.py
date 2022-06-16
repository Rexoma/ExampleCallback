import os

HELP_TXT = """
𝙷𝙴𝚈 {mention}
𝙷𝙴𝚁𝙴 𝙸𝚂 𝙼𝚈 𝙷𝙴𝙻𝙿 𝙼𝙴𝙽𝚄 𝙵𝙾𝚁 𝚈𝙾𝚄:
"""

ADMIN_TXT = """
**𝙷𝚎𝚕𝚙 𝙵𝚘𝚛 𝙰𝚍𝚖𝚒𝚗 𝙼𝚘𝚍𝚞𝚕𝚎:**

Make it easy to promote and demote with admin module!

USAGE:
➢ /promote - Promote an user as admin.
➢ /promote [title] - Promote an user with title.
➢ /spromote - Silently promote an user as admin.
➢ /demote - Demote an promoted admin.
➢ /sdemote - Silently demote an admin.
➢ /fpromote - Promote an user with all rights.
➢ /set_title - Set or change title of an admin.
➢ /admincache - Force refresh the admins list.

NOTE:
• Innexia should have admin privillage.
• Only admins can execute these in a chat.
• These commands can be used only in group.
""" 

AFK_TEXT = """
**𝙷𝚎𝚕𝚙 𝙵𝚘𝚛 𝙰𝚏𝚔 𝙼𝚘𝚍𝚞𝚕𝚎:**

Away From Keyboard is to tell that you're not available!

USAGE:
➢ /afk - Mark yourself as afk.
➢ /afk [reason] - Mark yourself as afk with reason.
➢ brb [reason] - Same as the afk command, but not a command.

NOTE:
• Innexia should have admin privillage.
• These commands can be used only in group.
• These commands can be used by any group member.
"""
 
CARBON_TXT = """
**𝙷𝚎𝚕𝚙 𝙵𝚘𝚛 𝙲𝚊𝚛𝚋𝚘𝚗 𝙼𝚘𝚍𝚞𝚕𝚎:**

Beautify your code using carbon.now.sh!

USAGE:
➢ /carbon [text] - Create carbon from the given text.
➢ /carbon [reply] - Create carbon from the replied text.
➢ /carbon [text]|[colour] - Create carbon with custom colour.
➢ /carbon [reply] [colour] - Create carbon with custom colour.

NOTE:
• Innexia should have admin privillage.
• These commands works on both pm and group.
• These commands can be used by any group member.
"""
BAN_TXT = """
**𝙷𝙴𝙻𝙿 𝙵𝙾𝚁 𝙱𝙰𝙽 𝙼𝙾𝙳𝚄𝙻𝙴:**

Make it easy to ban and unban with ban module!

USAGE:
➢ /ban [reason] - Ban an user with reason.
➢ /kick [reason] - Kick an user with reason.
➢ /kick [ghosts] - Kick all deleted accounts of chat.
➢ /tban [reason] - Temporary ban an user with reason.
➢ /sban [reason] - Silently ban an user with reason.
➢ /dban [reason] - Delete message banning its sender.
➢ /dkick [reason] - Delete message kicking its sender.
➢ /skick [reason] - Silently kick an user with reason.
➢ /unban - Unban an banned user or channel.
➢ /sunban - Silently unban an banned user or channel.

NOTE:
• Innexia should have admin privillage.
• Only admins can execute these in a chat.
• These commands can be used only in group.
"""

CONNECT_TXT = """
**𝙷𝚎𝚕𝚙 𝙵𝚘𝚛 𝙲𝚘𝚗𝚗𝚎𝚌𝚝 𝙼𝚘𝚍𝚞𝚕𝚎:**

Connect bot to your PM to avoid spamming in groups!

USAGE:
➢ /connect - Connect a specific chat.
➢ /disconnect - Disconnect from a chat.
➢ /connections - View your all connections.

NOTE:
• Innexia should have admin privillage.
• Only group admins can add a connection.
• Send /connect for connect me to ur PM
"""
FILTER_TXT = """
**𝙷𝚎𝚕𝚙 𝙵𝚘𝚛 𝙵𝚒𝚕𝚝𝚎𝚛 𝙼𝚘𝚍𝚞𝚕𝚎:**

Manual Filter is the feature where users can set automated replies for a particular keyword and bot will respond whenever a keyword is found the message!

USAGE:
➢ /filter - Add a filter in the chat.
➢ /filters - View all the filters of the chat.
➢ /stop - Delete a specific filter in the chat.
➢ /stopall - Delete all filters in the chat. (chat owner only)

NOTE:
• Innexia should have admin privillage.
• Only admins can add filters in a chat.
• Alert buttons have a limit of 64 characters.
"""
EXTRA_TXT = """
**𝙷𝙴𝙻𝙿 𝙵𝙾𝚁 𝙴𝚇𝚃𝚁𝙰 𝙼𝙾𝙳𝚄𝙻𝙴:**

There are some of mine extra features, enjoy!

USAGE:
➢ /read - Read texts from any image.
➢ /react - Add react button to message.
➢ /write - Write text as handwriting.
➢ /imdb - Get the film info from IMDb.
➢ /proxy - Get active mtproto proxies.
➢ /genstr - Generate pyrogram session.
➢ /qfancy - Get quotes from QuoteFancy.
➢ /download - Download files by direct link.

NOTE:
• Innexia should have admin privillage.
• These commands works on both pm and group.
• These commands can be used by any group member.

FILTER_TXT = 

LOCK_TXT = """

MUSIC_TXT = """

NOTE_TXT = 
RULE_TXT =
TOOL_TXT = 
USER_TXT = """

WELCOME_TXT = """
**𝙷𝚎𝚕𝚙 𝙵𝚘𝚛 𝚆𝚎𝚕𝚌𝚘𝚖𝚎 𝙼𝚘𝚍𝚞𝚕𝚎:**
Greet the new group members with welcome module!

USAGE:
➢ /welcome [on] - Enable welcome message.
➢ /welcome [off] - Disable welcome message.
➢ /captcha [on] - Enable welcome captcha.
➢ /captcha [off] - Disable welcome captcha.
➢ /setwelcome - Set a new welcome message.
➢ /getwelcome - Get current welcome message.
➢ /resetwelcome - Reset welcome message to default.

NOTE:
• Innexia should have admin privillage.
• Only admins can execute these in a chat.
• These commands can be used only in group.
