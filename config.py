import os

class Config():
    REGISTERED_USERS = {
    'eros@gmail.com': {"name": "Eduardo", "password": "123"},
    'jfitz@gmail.com': {"name": "Jackie", "password": "abc"},
    'gman@gmail.com': {"name": "Man", "password": "abc123"}
    }
    SECRET_KEY = os.environ.get("SECRET_KEY") or "you-will-never-guess"
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get("SQLALCHEMY_TRACK_MODIFICATIONS")
