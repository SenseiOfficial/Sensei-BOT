#IMG CREDITS: @Sensei_nex
#some symbols credits goes tp @kraken_the_badass
import asyncio
from telethon import events
from uniborg.util import admin_cmd
from userbot import ALIVE_NAME
from telethon.tl.types import ChannelParticipantsAdmins
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Senseibot user"
PM_IMG = "https://telegra.ph/file/023df30443809b46e0843.mp4"
pm_caption = "`⚠️HΞЯΞ CФMΞS ΓHΞ G.Ф.Д.Γ. SΞИSΞIБФΓ⚠️\n"
pm_caption += "`                   【🛡️ 𝕾𝖞𝖘𝖙𝖊𝖒 𝖘𝖙𝖆𝖙𝖚𝖘 🛡️】  `\n\n"
pm_caption += "`🔱─ᴛᴇʟᴇᴛʜᴏɴ─🔱       : `**6.0.9**\n` 💎 Python 💎:` **3.8.5**\n"
pm_caption += "`⚠️─ᴄᴜʀʀᴇɴᴛ ʙʀᴀɴᴄʜ─⚠️`: `↼🄼🄰🅂🅃🄴🅁⇀`\n"
pm_caption += "`⚜️─ѕєиѕєιвσт─⚜️      : `3.0`\n"
pm_caption += f"♾ ᴍʏ ʟɪᴇɢᴇ ♾       : {DEFAULTUSER} \n"
pm_caption += "✵─ᴍʏ ᴅᴇᴠ─✵          : [✞R.I.P.✞](https://t.me/sensei_nex)\n\n"
pm_caption += "✮ License ✮         : [♛SΞИSΞIБФΓ♛](https://github.com/SenseiOfficial/Sensei-BOT/blob/master/LICENSE)\n"

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
    
