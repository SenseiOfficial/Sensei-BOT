from pathlib import Path
from sys import argv

import telethon.utils
from telethon import TelegramClient

from userbot import bot
from userbot.utils import load_module
from var import Var


async def add_bot(bot_token):
    await bot.start(bot_token)
    bot.me = await bot.get_me()
    bot.uid = telethon.utils.get_peer_id(bot.me)


if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    if Var.TG_BOT_USER_NAME_BF_HER is not None:
        print(" Initiating Inline Bot ")
        # ForTheGreatrerGood of beautification
        bot.tgbot = TelegramClient(
            "TG_BOT_TOKEN", api_id=Var.APP_ID, api_hash=Var.API_HASH
        ).start(bot_token=Var.TG_BOT_TOKEN_BF_HER)
        print(
            "Initialisation finished with no errors , Your ⚜️─ѕєиѕєιвσт─⚜️ will be ready in sometime"
        )
        print("Starting SᗴᑎᔕᗴᎥbot")
        bot.loop.run_until_complete(add_bot(Var.TG_BOT_USER_NAME_BF_HER))
        print("ᔕᗴᑎᔕᗴᎥbot's Startup Completed")
    else:
        bot.start()


import glob

path = "userbot/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        load_module(shortname.replace(".py", ""))


print(
    " ⇋【The G.O.A.T. ⚜️─ѕєиѕєιвσт─⚜️ is on fire 🔥. Check .alive to test that bot is functioning or not . 】⇌ "
)

if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.run_until_disconnected()
