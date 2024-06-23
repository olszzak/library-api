from fastapi import Depends
from sqlalchemy.orm import Session

from app.borrow.schema import CreateBorrowSchema
from app.misc.db_base_service import BaseService
from app.misc.deps import get_db
from app.borrow.model import Borrow


class BorrowService(BaseService[Borrow, CreateBorrowSchema]):
    def __init__(self, db_session: Session):
        super(BorrowService, self).__init__(Borrow, db_session)

    def delete_by_user_book(self, user_id: str, book_id: str) -> None:
        obj = self.get_by_details(user_id=user_id, book_id=book_id)
        self.db_session.delete(obj)
        self.db_session.commit()


def get_borrow_service(db_session: Session = Depends(get_db)) -> BorrowService:
    return BorrowService(db_session)
