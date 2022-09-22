import os
import re
from flask import Flask
from flask_pymongo import PyMongo
from flask_sqlalchemy import SQLAlchemy
from omdb import OMDBClient
if os.path.exists("env.py"):
    import env  # noqa


app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.config["API_KEY"] = os.environ.get("API_KEY")

if os.environ.get("DEVelopment") == "True":
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")

db = SQLAlchemy(app)
mongo = PyMongo(app)
api_key = os.environ.get("API_KEY")

# omdb movie search key
# documentation can be found at https://pypi.org/project/omdb/
client = OMDBClient(apikey=api_key)

from movielounge import routes  # noqa
