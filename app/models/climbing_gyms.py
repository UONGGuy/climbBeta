# app/models/climbing_gyms.py
from app import db
from app.models.base_model import BaseModel
from app.models.enums import eFranchiser
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List

# Relationship hierarchy
# Franchiser >> ClimbingGym >> Features

class Franchiser(BaseModel):
    # Model defining franchisers of climbing gyms
    name: Mapped[eFranchiser] = mapped_column(db.Enum(eFranchiser), nullable=False)
    climbing_gyms: Mapped[List['ClimbingGym']] = relationship('ClimbingGym', backref='franchiser', lazy=True)

    def __init__(self, name: eFranchiser):
        super().__init__()
        self.name = name


class ClimbingGym(BaseModel):
    """Model initialising ClimbingGym object
    
    Keyword arguments:
    name: str -- Climbing Gym name
    franchiser_id: int -- Franchiser unique ID
    
    Return: none
    """
    
    name: Mapped[str] = mapped_column(db.String(100), nullable=False) # Climbing Gym name
    franchiser_id: Mapped[int] = mapped_column(db.ForeignKey('franchiser.id')) # Franchiser unique ID

    def __init__(self, name: str, franchiser: eFranchiser):
        super().__init__()
        self.name = name
        self.franchiser = franchiser
        self.boards = []