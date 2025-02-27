# app/models/__init__.py
# Import all classes to be assigned under the model file initialisation
from app.models.association_tables import *
from app.models.climbing_gyms import *
from app.models.climbing_gym_features import *
from app.models.enums import *
from sqlalchemy.orm import relationship

# Define all object relationships

# Climbing boards
ClimbingGym.boards = relationship('ClimbingBoard', secondary=climbing_boards_map, back_populates='climbing_gyms')
ClimbingBoard.climbing_gyms = relationship('ClimbingGym', secondary=climbing_boards_map, back_populates='boards')