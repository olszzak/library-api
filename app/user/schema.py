from pydantic import BaseModel

from app.borrow.schema import BorrowSchema


class UserSchema(BaseModel):
    id: str
    name: str
    borrowed: None | list[BorrowSchema]


class CreateUserSchema(BaseModel):
    id: str
    name: str
