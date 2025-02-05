# app/models.py
from app import db
from app.enums import eClimbBoard, eFranchiser
from sqlalchemy.orm import Mapped, mapped_column

class BaseModel(db.Model):
    __abstract__ = True # Define so is not created as table in database

    id: Mapped[int] = mapped_column(primary_key=True) # Primary key

    def __repr__(self):
        # Generate string representation iterating over model columns with getattr
        fields = ", ".join(f"{attr}={getattr(self, attr)!r}" for attr in self.__table__.columns.keys())
        return f"<{self.__class__.__name__}({fields})>"


class ClimbingGym(BaseModel):
    """ Model defining climbing gyms.

        ClimbingGym(name: str, franchiser_id: int)
    """
    name: Mapped[str] = mapped_column(db.String(100), nullable=False) # Name
    # location = mapped_column(db.String(200), nullable=False)

    # Backrefs 
    # franchiser

    franchiser_id: Mapped[int] = mapped_column(db.ForeignKey('franchiser.id'))

    # Many-to-Many relationships
    boards = db.relationship('ClimbingBoard', secondary='climbing_boards_map', back_populates='climbing_gyms')


class Franchiser(BaseModel):
    # Model defining franchisers of climbing gyms
    name: Mapped[eFranchiser] = mapped_column(db.Enum(eFranchiser), nullable=False)
    climbing_gyms = db.relationship('ClimbingGym', backref='franchiser', lazy=True)


class ClimbingBoard(BaseModel):
    # Model defining climbing boards a climbing gym may have
    board_type: Mapped[eClimbBoard] = mapped_column(db.Enum(eClimbBoard), nullable=False)
    is_adjustable: Mapped[bool] = mapped_column(db.Boolean, nullable=False)
    angle_of_incline: Mapped[float] = mapped_column(db.Float, nullable=False)

    # Many-to-Many relationship with ClimbingGym
    climbing_gyms = db.relationship('ClimbingGym', secondary='climbing_boards_map', back_populates='boards')

class ClimbingBoardsMap(db.Model):
    # Map climbing boards to climbing gyms
    __tablename__ = 'climbing_boards_map'
    climbing_gym_id: Mapped[int] = mapped_column(db.Integer, db.ForeignKey('climbing_gym.id'), primary_key=True)
    board_id: Mapped[int] = mapped_column(db.Integer, db.ForeignKey('climbing_board.id'), primary_key=True)


