# config/testing.py

class TestingConfig:
    DEBUG = False
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:' # In-memory SQLite
    SQLALCHEMY_TRACK_MODIFICATIONS = False

