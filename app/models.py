# app/models.py
from app import db
from app.enums import eClimbBoard

class ClimbingGym(db.Model):
    id = db.Column(db.Integer, primary_key=True) # Primary key
    name = db.Column(db.String(100), nullable=False) # Climbing gym name
    # location = db.Column(db.String(200), nullable=False)

    # Many-to-Many relationship with ClimbingBoard
    climb_boards = db.relationship('ClimbingBoard', secondary='climbing_boards_map', back_populates='climbing_gyms')

class ClimbingBoard(db.Model):
    # Model defining climbing boards a climbing gym may have
    id = db.Column(db.Integer, primary_key=True)
    board_type = db.Column(db.Enum(eClimbBoard), nullable=False)
    is_adjustable = db.Column(db.Boolean, nullable=False)
    angle_of_incline = db.Column(db.Float, nullable=False)

    # Many-to-Many relationship with ClimbingGym
    climbing_gyms = db.relationship('ClimbingGym', secondary='climbing_boards_map', back_populates='climb_boards')

class ClimbingBoardsMap(db.Model):
    # Map climbing boards to climbing gyms
    __tablename__ = 'climbing_boards_map'
    climbing_gym_id = db.Column(db.Integer, db.ForeignKey('climbing_gym.id'), primary_key=True)
    board_id = db.Column(db.Integer, db.ForeignKey('climbing_board.id'), primary_key=True)
