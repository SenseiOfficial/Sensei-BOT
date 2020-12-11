#IMG CREDITS: @Sensei_nex
import asyncio
from telethon import events
from uniborg.util import admin_cmd
from userbot import ALIVE_NAME
from telethon.tl.types import ChannelParticipantsAdmins
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Senseibot user"
PM_IMG = "https://telegra.ph/file/023df30443809b46e0843.mp4"
pm_caption = "🔺`🔥⚠️HΞЯΞ CФMΞS ΓHΞ G.Ф.Д.Γ. SΞИSΞIБФΓ⚠️🔥\n\n"
pm_caption += "🔻`S҉Y҉S҉T҉E҉M҉ ҉S҉T҉A҉T҉U҉S҉`\n"
pm_caption += "🔺`T̳̿͟͞E̳̿͟͞L̳̿͟͞E̳̿͟͞T̳̿͟͞H̳̿͟͞O̳̿͟͞N̳̿͟͞ ̳̿͟͞V̳̿͟͞E̳̿͟͞R̳̿͟͞S̳̿͟͞I̳̿͟͞O̳̿͟͞N̳̿͟͞:` **6.0.9**\n` ♾Python:` **3.8.5**\n"
pm_caption += "🔻`D̳̿͟͞A̳̿͟͞T̳̿͟͞A̳̿͟͞B̳̿͟͞A̳̿͟͞S̳̿͟͞E̳̿͟͞ ̳̿͟͞S̳̿͟͞T̳̿͟͞A̳̿͟͞T̳̿͟͞U̳̿͟͞S̳̿͟͞:` **Functional**\n"
pm_caption += "🔶`C̳̿͟͞u̳̿͟͞r̳̿͟͞r̳̿͟͞e̳̿͟͞n̳̿͟͞t̳̿͟͞ ̳̿͟͞B̳̿͟͞r̳̿͟͞a̳̿͟͞n̳̿͟͞c̳̿͟͞h̳̿͟͞` : `master`\n"
pm_caption += "🔷*ᔕᗴᑎᔕᗴᎥᗰᗩ᙭ OS** : `2.14`\n"
pm_caption += f"🔹**My Boss** : {DEFAULTUSER} \n"
pm_caption += "🔸**MAh Lord 😎 : [This nub](https://t.me/sensei_nex)\n\n"
pm_caption += "👀 Wanna have your own [Senseibot](https://github.com/SenseiOfficial/Sensei-BOT)\n"

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
    
