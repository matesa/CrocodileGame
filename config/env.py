from os import getenv

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = getenv('BOT_TOKEN')
MONGO_URI = getenv('MONGO_URI')
SUDO_USERS = list(map(int, getenv('SUDO_USERS').split()))
