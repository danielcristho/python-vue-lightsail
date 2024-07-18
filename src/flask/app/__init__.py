from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from app.config import DB_URL
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL

db = SQLAlchemy(app)

from app import routes
