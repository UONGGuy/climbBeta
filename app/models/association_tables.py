# app/models/association_tables.py
from app import db

# Association table between ClimbingGym and ClimbingBoard
climbing_boards_map = db.Table(
    'climbing_boards_map',
    db.Column('climbing_gym_id', db.Integer, db.ForeignKey('climbing_gym.id'), primary_key=True),
    db.Column('climbing_board_id', db.Integer, db.ForeignKey('climbing_board.id'), primary_key=True)
)