from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from app.config import DEV_DB, PROD_DB
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DEV_DB
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

CORS(app, resources={r'/*': {'origins': '*'}})

db = SQLAlchemy(app)

from app import routes