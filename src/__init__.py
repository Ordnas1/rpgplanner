"""Inits app"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy.orm import DeclarativeBase

from .config import config


class Base(DeclarativeBase):
    """Base declarative base"""
    pass


db = SQLAlchemy(model_class=Base)
migrate = Migrate()


def create_app(config_mode):
    """Instantiates initial app elements"""
    app = Flask(__name__)
    app.config.from_object(config[config_mode])

    db.init_app(app)
    migrate.init_app(app, db)

    return app
