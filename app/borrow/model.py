from sqlalchemy import Column, String, ForeignKey, DateTime, func

from app.misc.db import Base


class Borrow(Base):
    __tablename__ = "borrow"

    book_id = Column(String, ForeignKey("book.id"), primary_key=True)
    user_id = Column(String, ForeignKey("user.id"), primary_key=True)
    borrowed_at = Column(DateTime, server_default=func.now())
