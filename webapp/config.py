from secrets import token_urlsafe
from datetime import timedelta

class Config(object):
    DEBUG = False
    TESTING = False

    # Set a safe secret key
    SECRET_KEY = token_urlsafe(18)

    SQLALCHEMY_DATABASE_URI = 'sqlite:///baseModel.sqlite3'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Only allow HTTPS secure connection
    SESSION_COOKIE_SECURE = True
    # Set session variable to last only for 5 mintues instead of 30 days.
    PERMANENT_SESSION_LIFETIME = timedelta(minutes=60)

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEBUG = True
    SESSION_COOKIE_SECURE = False

class TestingConfig(Config):
    TESTING = True
    SESSION_COOKIE_SECURE = False
