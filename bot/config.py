from bot.get_cfg import get_config

class Config(object):
    # You can keep this default
    SESSION_NAME = get_config("SESSION_NAME", "EncoderX") 
    # EncoderX_bot....
    # sucks Dude
    APP_ID = int(get_config("APP_ID", "26387127"))
    API_HASH = get_config("API_HASH", "19718ab7acd97d0f71ada2807ddfe47a")
    LOG_CHANNEL = get_config("LOG_CHANNEL", "RulfEncoderLogs")
    UPDATES_CHANNEL = get_config("UPDATES_CHANNEL", None) # Without `@` LOL
     # Get these values from my.telegram.org
    AUTH_USERS = [-1001934483724, 5446367898]
# array , simplest method was AUTH_USERS = [] ; AUTH_USERS.append(your telegram id) 🌹
    TG_BOT_TOKEN = get_config("TG_BOT_TOKEN", "7257386978:AAGoHTntoUEbi2A3emmIu3R5zHGrXlydpLM")
    # the download location, where the HTTP Server runs
    DOWNLOAD_LOCATION = get_config("DOWNLOAD_LOCATION", "/app/downloads")
    # Telegram maximum file upload size
    BOT_USERNAME = get_config("BOT_USERNAME", "Alya_encoder_bot")
    MAX_FILE_SIZE = 4194304000
    TG_MAX_FILE_SIZE = 4194304000
    FREE_USER_MAX_FILE_SIZE = 4194304000
    # default thumbnail to be used in the videos
    DEF_THUMB_NAIL_VID_S = get_config("DEF_THUMB_NAIL_VID_S", "https://placehold.it/90x90")
    # proxy for accessing youtube-dl in GeoRestricted Areas
    # Get your own proxy from https://github.com/rg3/youtube-dl/issues/1091#issuecomment-230163061
    HTTP_PROXY = get_config("HTTP_PROXY", None)
    # maximum message length in Telegram
    MAX_MESSAGE_LENGTH = 4096
    # add config vars for the display progress
    FINISHED_PROGRESS_STR = get_config("FINISHED_PROGRESS_STR", "")
    UN_FINISHED_PROGRESS_STR = get_config("UN_FINISHED_PROGRESS_STR", "")
    LOG_FILE_ZZGEVC = get_config("LOG_FILE_ZZGEVC", "Log.txt")
    SHOULD_USE_BUTTONS = get_config("SHOULD_USE_BUTTONS", False)
