from http import HTTPStatus

from fastapi import APIRouter, Depends

from app.book.schema import BookSchema, CreateBookSchema
from app.book.service import get_books_service, BookService

router = APIRouter(tags=["book"])


@router.post("/books/", response_model=BookSchema, status_code=HTTPStatus.CREATED)
def create_book(
    book: CreateBookSchema, book_service: BookService = Depends(get_books_service)
):
    return book_service.create(book)


@router.get("/books/", response_model=list[BookSchema])
def read_books(book_service: BookService = Depends(get_books_service)):
    return book_service.list()


@router.delete("/books/{book_id}", status_code=HTTPStatus.NO_CONTENT)
def delete_book(book_id: str, book_service: BookService = Depends(get_books_service)):
    return book_service.delete(book_id)
