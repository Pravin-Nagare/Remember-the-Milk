from flask import Flask
from flaskext.mongoalchemy import MongoAlchemy
import string

app = Flask(__name__)
app.config['MONGOALCHEMY_DATABASE'] = 'task_collection'
app.config['SECRET_KEY'] = 'very secret, do you believe?'
app.config['DEBUG'] = True
db = MongoAlchemy(app)

from views import *
