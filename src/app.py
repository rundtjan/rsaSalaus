from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import fixforheroku

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = fixforheroku.uri
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return user_service.get_user(user_id)

import routes

import db_init
