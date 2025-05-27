"""
from os import getenv


API_ID = int(getenv("API_ID", "27262405"))
API_HASH = getenv("API_HASH", "33011215edbd8c0f6b710df2fdf0b088")
BOT_TOKEN = getenv("BOT_TOKEN", "7822925118:AAH3am8r4RopB0NQrfj71FVNBZyd2KEbH1Q")
OWNER_ID = int(getenv("OWNER_ID", "6768714745"))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6768714745").split()))
MONGO_URL = getenv("MONGO_DB", "mongodb+srv://vikassonawale0:JWyQFas7vlG1bkaL@cluster0.beermge.mongodb.net/?retryWrites=true&w=majority")

CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002609761797"))
PREMIUM_LOGS = int(getenv("PREMIUM_LOGS", "-1002526911796"))

"""
#




# --------------M----------------------------------

import os
from os import getenv
# ---------------R---------------------------------
API_ID = int(os.environ.get("API_ID", "27262405"))
# ------------------------------------------------
API_HASH = os.environ.get("API_HASH", "33011215edbd8c0f6b710df2fdf0b088")
# ----------------D--------------------------------
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7822925118:AAH3am8r4RopB0NQrfj71FVNBZyd2KEbH1Q")
# -----------------A-------------------------------
BOT_USERNAME = os.environ.get("Vikassonawale_bot")
# ------------------X------------------------------
OWNER_ID = int(os.environ.get("OWNER_ID", "6768714745"))
# ------------------X------------------------------

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6768714745").split()))
# ------------------------------------------------
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002609761797"))
# ------------------------------------------------
MONGO_URL = os.environ.get("MONGO_URL", "mongodb+srv://vikassonawale0:JWyQFas7vlG1bkaL@cluster0.beermge.mongodb.net/?retryWrites=true&w=majority")
# -----------------------------------------------
FORCE_SUB = int(os.environ.get("FORCE_SUB", "-1002372063544"))

