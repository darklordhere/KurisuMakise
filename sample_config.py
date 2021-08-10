# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
from KurisuMakise import FARIS, MAKISE_OWN, MAYURI, RINTAROU, SUZUHA
import json
import os


def get_user_list(config, key):
    with open('{}/SaitamaRobot/{}'.format(os.getcwd(), config),
              'r') as json_file:
        return json.load(json_file)[key]


# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True
    # REQUIRED
    #Login to https://my.telegram.org and fill in these slots with the details given by it

    
    API_ID = 123456  # integer value, dont use ""
    API_HASH = "awoo"
    TOKEN = "BOT_TOKEN"  #This var used to be API_KEY but it is now TOKEN, adjust accordingly.
    OWNER_ID = 792109647  # If you dont know, run the bot and do /id in your private chat with it, also an integer
    OWNER = 792109647
    SUPPORT_CHAT = 'OnePunchSupport'  #Your own group for support, do not add the @

    #RECOMMENDED
    REDIS_URI = " "
    LOAD = []
    NO_LOAD = ['rss', 'cleaner', 'connection', 'math']

    #OPTIONAL
    ##List of id's -  (not usernames) for users which have sudo access to the bot.
    MAKISE_OWN = get_user_list('elevated_users.json', 'sudos')
    ##List of id's - (not usernames) for developers who will have the same perms as the owner
    RINTAROU = get_user_list('elevated_users.json', 'devs')
    ##List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    MAYURI = get_user_list('elevated_users.json', 'supports')
    #List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    SUZUHA = get_user_list('elevated_users.json', 'tigers')
    FARIS = get_user_list('elevated_users.json', 'whitelists')
    DEL_CMDS = True  #Delete commands that users dont have access to, like delete /ban if a non admin uses it.
    WORKERS = 8  # Number of subthreads to use. Set as number of threads your processor uses
    WALL_API = 'awoo'  #For wallpapers, get one from https://wall.alphacoders.com/api.php
    AI_API_KEY = 'awoo'  #For chatbot, get one from https://coffeehouse.intellivoid.net/dashboard

class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
