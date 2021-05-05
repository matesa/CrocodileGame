from telegram.ext import Filters

from config import SUDO_USERS

sudo_only = Filters.user(SUDO_USERS)
