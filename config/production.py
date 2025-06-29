# config/production.py

class ProductionConfig:
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///climbbeta.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

