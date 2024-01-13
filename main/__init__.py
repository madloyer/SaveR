#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = 14426508
API_HASH = "e44bc81e970faf1a15fea053d02c6cb7"
BOT_TOKEN = "6494673462:AAFLjjxGOYxDyuShBKVLP6ZQD_HyNyg533o"
SESSION = "1AZWarzkBu2HCnFcH9qCMPk8ZxEbWfSb3CdI340C36y9PZr5fQTmZSWVxx_7UEmjbvA6FLo_hE-HENLeuIdzJjijyeq1Lce9Ps8dDCnFhmiXx6isxhEehRwkg2GmMgGabaN-eQiHvqN1dlNsfv8tgmqgBDUC4TEbw1niKtw2i8hpZHVJXXcWnzjoO-pmiGwSgSfvuH_ZR6cX-YmDjZ3wH7iefNMhUnUZV1_T8OvqXQYGYeZruUJvr1JuRX0a5XBl4sJjqr45VikN-vaXxk9pWQPjze0w0UaP8QFHKAfVNhBisWx-NrTglwuE6MImbDzbEfLTinDNWTzYkZHso9nUypbkABlBFfco="
FORCESUB = "mantapvids"
AUTH = 5102999288

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("saverkontenbot", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "saverkontenbot",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
