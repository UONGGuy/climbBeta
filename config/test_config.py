# test_config.py

class TestConfig:
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:' # In-memory SQLite
    SQLALCHEMY_TRACK_MODIFICATIONS = False

