# database/drop_tables.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import create_app, db

app = create_app()

with app.app_context():
    print("Dropping all tables...")
    db.drop_all()
    print("All tables dropped.")
    print("Creating all tables...")
    db.create_all()
    print("All tables created.")
