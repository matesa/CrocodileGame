from pymongo import MongoClient

from config import MONGO_URI

client = MongoClient(MONGO_URI)
database = client.crocodile_game_bot
