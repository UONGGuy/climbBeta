# app/models/climbing_gym_features.py
from app import db
from app.models.base_model import BaseModel
from app.models.enums import eClimbBoard
from sqlalchemy.orm import Mapped, mapped_column

# Relationship hierarchy
# Franchiser >> ClimbingGym >> Features

class ClimbingBoard(BaseModel):
    # Model defining climbing boards a climbing gym may have
    board_type: Mapped[eClimbBoard] = mapped_column(db.Enum(eClimbBoard), nullable=False)
    is_adjustable: Mapped[bool] = mapped_column(db.Boolean, nullable=False)
    angle_of_incline: Mapped[float] = mapped_column(db.Float, nullable=False)

    def __init__(self, board_type: eClimbBoard, is_adjustable: bool, angle_of_incline: float):
        super().__init__()
        self.board_type = board_type
        self.is_adjustable = is_adjustable
        self.angle_of_incline = angle_of_incline
        self.climbing_gyms = []
