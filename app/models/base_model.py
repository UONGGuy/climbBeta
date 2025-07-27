# app/models/base_model.py
from app import db
from sqlalchemy.ext.declarative import as_declarative
from sqlalchemy.orm import Mapped, mapped_column

@as_declarative()
class BaseModel(db.Model):
    __abstract__ = True # Define so is not created as table in database

    id: Mapped[int] = mapped_column(primary_key=True) # Primary key

    def __init__(self):
        super().__init__()

    def __repr__(self):
        # Generate string representation iterating over model columns with getattr
        fields = ", ".join(f"{attr}={getattr(self, attr)!r}" for attr in self.__table__.columns.keys())
        return f"<{self.__class__.__name__}({fields})>"
