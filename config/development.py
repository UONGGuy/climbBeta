# config/development.py

class DevelopmentConfig:
    DEBUG = True
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///climbbeta.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
