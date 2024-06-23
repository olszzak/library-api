from fastapi import Depends
from sqlalchemy.orm import Session

from app.book.schema import CreateBookSchema
from app.misc.db_base_service import BaseService
from app.misc.deps import get_db
from app.book.model import Book


class BookService(BaseService[Book, CreateBookSchema]):
    def __init__(self, db_session: Session):
        super(BookService, self).__init__(Book, db_session)


def get_books_service(db_session: Session = Depends(get_db)) -> BookService:
    return BookService(db_session)
