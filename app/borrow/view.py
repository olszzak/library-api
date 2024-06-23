from http import HTTPStatus

from fastapi import APIRouter, Depends

from app.borrow.schema import CreateBorrowSchema
from app.borrow.service import get_borrow_service, BorrowService

router = APIRouter(tags=["borrow"])


@router.post("/books/{book_id}/users/{user_id}", status_code=HTTPStatus.CREATED)
def add_user_to_book(
    book_id: str,
    user_id: str,
    borrow_service: BorrowService = Depends(get_borrow_service),
):
    borrow_service.create(CreateBorrowSchema(user_id=user_id, book_id=book_id))


@router.post("/users/{user_id}/books/{book_id}", status_code=HTTPStatus.CREATED)
def add_book_to_user(
    book_id: str,
    user_id: str,
    borrow_service: BorrowService = Depends(get_borrow_service),
):
    borrow_service.create(CreateBorrowSchema(user_id=user_id, book_id=book_id))


@router.delete("/users/{user_id}/books/{book_id}", status_code=HTTPStatus.NO_CONTENT)
def delete_book_to_user(
    book_id: str,
    user_id: str,
    borrow_service: BorrowService = Depends(get_borrow_service),
):
    borrow_service.delete_by_user_book(user_id=user_id, book_id=book_id)


@router.delete("/books/{book_id}/users/{user_id}", status_code=HTTPStatus.NO_CONTENT)
def delete_user_to_book(
    book_id: str,
    user_id: str,
    borrow_service: BorrowService = Depends(get_borrow_service),
):
    borrow_service.delete_by_user_book(user_id=user_id, book_id=book_id)
