from pydantic import BaseModel

from app.borrow.schema import BorrowSchema


class BookSchema(BaseModel):
    id: str
    title: str
    author: str
    borrowed: None | list[BorrowSchema]


class CreateBookSchema(BaseModel):
    id: str
    title: str
    author: str
