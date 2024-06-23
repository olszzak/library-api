from sqlalchemy import Column, String
from sqlalchemy.orm import validates, relationship

from app.misc.db import Base
from app.borrow.model import Borrow  # noqa


class User(Base):
    __tablename__ = "user"

    id = Column(String, primary_key=True)
    name = Column(String, nullable=False)

    borrowed = relationship("Borrow")

    @validates("id")
    def validate_id(self, _, value):
        if len(value) != 6:
            raise ValueError("id must be a 6-digit integer")
        if not value.isdigit():
            raise ValueError("id must contains only integers")
        return value
