from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

from .config import config_by_name

db = SQLAlchemy()
bcrypt = Bcrypt()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    #app.config['SQLALCHEMY_ECHO'] = config_by_name[config_name].DEBUG
    db.init_app(app)
    bcrypt.init_app(app)
    return app
