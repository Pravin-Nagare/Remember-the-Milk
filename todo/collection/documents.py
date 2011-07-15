from collection import db
from flaskext.mongoalchemy import BaseQuery
import datetime


class Task(db.Document):
    task = db.StringField()
    start = db.IntField()
    time =db.IntField()
