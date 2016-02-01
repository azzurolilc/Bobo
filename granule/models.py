from __future__ import unicode_literals

from pymongo import MongoClient
# client = MongoClient('localhost',27017)
# client = MongoClient('mongodb://localhost:27017')

from mongoengine import *
from django.db import models
import datetime

# Create your models here.

class Employee(Document):
    email = StringField(required=True)
    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)

class Choice(EmbeddedDocument):
    choice_text = StringField(max_length=200)
    votes = IntField(default=0)

class Poll(Document):
    question = StringField(max_length=200)
    pub_date = DateTimeField(default=datetime.datetime.now,require=True,help_text='date published')
    choices = ListField(EmbeddedDocumentField(Choice))

    meta = {
        'indexes': [
            'question', 
            ('pub_date', '+question')
        ]
    }