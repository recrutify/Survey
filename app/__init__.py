from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

from flask.ext.heroku import Heroku
import logging
import sys


app = Flask(__name__)
app.config.from_pyfile('../config.py')

app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)
heroku = Heroku(app)
db = SQLAlchemy(app)

from app import views