#IMG CREDITS: @WhySooSerious
import asyncio
from telethon import events
from uniborg.util import admin_cmd
from userbot import ALIVE_NAME
from telethon.tl.types import ChannelParticipantsAdmins
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Senseibot user"
PM_IMG = "hhttps://telegra.ph/file/023df30443809b46e0843.mp4"
pm_caption = "🔺`⚠️Here comes the G.O.A.T. Senseibot⚠️\n\n"
pm_caption += "🔻**SYSTEM STATUS**\n"
pm_caption += "🔺`TELETHON VERSION:` **6.0.9**\n` ♾Python:` **3.8.5**\n"
pm_caption += "🔻`DATABASE STATUS:` **Functional**\n"
pm_caption += "🔶**Current Branch** : `master`\n"
pm_caption += "🔷*ᔕᗴᑎᔕᗴᎥᗰᗩ᙭ OS** : `2.14`\n"
pm_caption += f"🔹**My Boss** : {DEFAULTUSER} \n"
pm_caption += "🔸**MAh Lord 😎 : [This nub](https://t.me/sensei_nex)\n\n"
pm_caption += "👀 Wanna have your own [Senseibot]https://github.com/SenseiOfficial/Sensei-BOT)\n"

@borg.on(admin_cmd(pattern=r"alive"))
async def friday(alive):
    chat = await alive.get_chat()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG,caption=pm_caption)
    await alive.delete()

    
@borg.on(admin_cmd(pattern=r"Alive", allow_sudo=True))
async def friday(alive):
    chat = await alive.get_chat()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG,caption=pm_caption)
    
