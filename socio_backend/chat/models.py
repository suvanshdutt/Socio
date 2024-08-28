import datetime
from django.db import models

# Create your models here.

from pymongo import MongoClient
from django.conf import settings

client = MongoClient('mongodb://localhost:27017/')
db = client[settings.MONGO_DB_NAME]

class Chat:
    def __init__(self, participants):
        self.participants = participants
        self.messages = []
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def save(self):
        chat_data = {
            "participants": self.participants,
            "messages": self.messages,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }
        db.chats.insert_one(chat_data)
