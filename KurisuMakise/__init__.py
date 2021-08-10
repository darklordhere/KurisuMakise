#ANIMEMATRIX ALL RIGHTS RESERVED
import logging
import sys
import time
import telegram.ext as tg
import os
from pyrogram import Client
from telethon import TelegramClient
from redis import StrictRedis

StartTime = time.time()

# enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'),
              logging.StreamHandler()],
    level=logging.INFO)

LOGGER = logging.getLogger(__name__)

#ADMINS SETUP DON'T EDIT IF DON'T KNOW

    try:
        MAKISE_OWN = set(int(x) for x in os.environ.get("MAKISE_OWN", "").split()) #OWNER
        RINTAROU = set(int(x) for x in os.environ.get("RINTAROU", "").split()) #dev
    except ValueError:
       raise Exception("Your sudo or dev users list does not contain valid integers.")

    try:
        MAYURI = set(int(x) for x in os.environ.get("MAYURI", "").split()) #SUPPORT USERS
    except ValueError:
        raise Exception("Your support users list does not contain valid integers.")

    try:
        SUZUHA = set(int(x) for x in os.environ.get("SUZUHA", "").split()) #WHITELIST
    except ValueError:
        raise Exception("Your whitelisted users list does not contain valid integers.")

    try:
        FARIS = set(int(x) for x in os.environ.get("FARIS", "").split()) # PERMISSION TO BAN
    except ValueError:
        raise Exception("Your tiger users list does not contain valid integers.")


TRIGGERS = os.environ.get("TRIGGERS", "/ !").split(" ")
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")
BOT_NAME = os.environ.get("BOT_NAME")
DB_URL = os.environ.get("DATABASE_URL")
DB_URI = os.environ.get("DATABASE_URL")
API_ID = int(os.environ.get("API_ID"))
LOG_CHANNEL_ID = int(os.environ.get("LOG_CHANNEL_ID"))
OWNER = list(filter(lambda x: x, map(int, os.environ.get("OWNER_ID").split())))
OWNER_ID = list(filter(lambda x: x, map(int, os.environ.get("OWNER_ID").split())))   ## sudos can be included
WALL_API = os.environ.get("WALL_API", None)
SUPPORT_CHAT = os.environ.get("SUPPORT_CHAT", None)
WORKERS = int(os.environ.get("WORKERS", 8))
DOWN_PATH = "KurisuMakise/downloads/"
HELP_DICT = dict()
DEL_CMDS = bool(os.environ.get("DEL_CMDS", False))
REDIS_URL = os.environ.get("REDIS_URL")
LOAD = os.environ.get("LOAD", "").split()
NO_LOAD = os.environ.get("NO_LOAD", "translation").split()

#DEFINE DON'T EDIT ANYTHING
api_id = API_ID
api_hash = API_HASH
bot_token = BOT_TOKEN
tbot = TelegramClient('anon', api_id, api_hash).start(bot_token=bot_token)
plugins = dict(root="KurisuMakise/plugins")
KurisuMakise = Client("KurisuMakise", bot_token=BOT_TOKEN, api_id=API_ID, api_hash=API_HASH, plugins=plugins)
#CLOSE HERE

REDIS = StrictRedis.from_url(REDIS_URL,decode_responses=True)
try:
    REDIS.ping()
    LOGGER.info("Your redis server is now alive!")
except BaseException:
    raise Exception("Your redis server is not alive, please check again.")
    
finally:
   REDIS.ping()
   LOGGER.info("Your redis server is now alive!")

#ADDING OWNER
MAKISE_OWN.add(OWNER_ID)
RINTAROU.add(OWNER_ID)


updater = tg.Updater(BOT_TOKEN, workers=WORKERS, use_context=True)
telethn = TelegramClient("KurisuMakise", API_ID, API_HASH)
tbot = TelegramClient('anon', api_id, api_hash).start(bot_token=bot_token)
dispatcher = updater.dispatcher

# Load at end to ensure all prev variables have been set
from KurisuMakise.plugins.helper_funcs.handlers import (
    CustomCommandHandler,
    CustomMessageHandler,
    CustomRegexHandler,
)

# make sure the regex handler can take extra kwargs
tg.RegexHandler = CustomRegexHandler
tg.CommandHandler = CustomCommandHandler
tg.MessageHandler = CustomMessageHandler