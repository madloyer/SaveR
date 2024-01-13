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
SESSION = "AQBQ8NMX7bfl93QDKncMzzJsKWHzDzcbAgToiv9MvNrbGhSOkjnjr06o9on3Qs3lKAzD4uReuAqE8ScxcQsmTC9vcUqms8mTNecMHtqzaLr6sONKrSDMmL4owNxnxeD0mddUpLoaXlFgW8EzUiaka78BAxEwzhxMx1csYHfCKgSnIJlyJO_d7LjCDfFdzwVzN8C8twDp7Up-ZutRsNHFqEUYMCHZ_hYRZ9A6T7Z0pF2LZHXmLKH2zV2SDwTfJAxzFvEqPnyq6H9kkaq8m-tG7edf90jfr48yzeA7Teyz3sfFTz9DQedKuxwwwEU46xV7aKz7O_SISjykOzsHLLG9y5PlUsh7CQA"
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
