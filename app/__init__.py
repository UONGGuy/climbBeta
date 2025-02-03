# app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config.config import Config
from config.test_config import TestConfig

db = SQLAlchemy()

def create_app(config_class=Config):
    print("Creating Flask app") # Debug
    app = Flask(__name__)
    app.config.from_object(config_class)
    db.init_app(app)

    with app.app_context():
        print("Creating database tables") # Debug
        db.create_all()

    from app.routes import register_routes
    register_routes(app)

    return app

