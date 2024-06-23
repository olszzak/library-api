from http import HTTPStatus

from fastapi import APIRouter, FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException

from app.book.view import router as book_router
from app.borrow.view import router as borrow_router
from app.misc.exception import LibraryApiError
from app.ping.view import router as ping_router
from app.settings import get_settings
from app.user.view import router as user_router

settings = get_settings()


def setup_routing(fastapi_app: FastAPI):
    global_router = APIRouter()
    global_router.include_router(ping_router)
    global_router.include_router(user_router)
    global_router.include_router(book_router)
    global_router.include_router(borrow_router)
    fastapi_app.include_router(global_router)


def setup_handlers(fastapi_app, debug: bool = False):
    @fastapi_app.exception_handler(LibraryApiError)
    async def library_api_exception_handler(_: Request, exc: LibraryApiError):
        return JSONResponse(
            status_code=exc.status_code,
            content={
                "message": exc.message
                + f"{f' Details: {exc.details}' if debug else ''}"
            },
        )

    @fastapi_app.exception_handler(RequestValidationError)
    async def request_exception_handler(_: Request, exc: RequestValidationError):
        return JSONResponse(
            status_code=HTTPStatus.BAD_REQUEST,
            content={
                "message": f"Something went wrong.{' Details: ' + str(exc) if debug else ''}"
            },
        )

    @fastapi_app.exception_handler(ValueError)
    async def value_exception_handler(_: Request, exc: ValueError):
        return JSONResponse(
            status_code=HTTPStatus.BAD_REQUEST,
            content={
                "message": f"Something went wrong.{' Details: ' + str(exc) if debug else ''}"
            },
        )

    @fastapi_app.exception_handler(StarletteHTTPException)
    async def starlette_exception_handler(_: Request, exc: StarletteHTTPException):
        return JSONResponse(
            status_code=HTTPStatus.SERVICE_UNAVAILABLE,
            content={
                "message": f"Something went wrong. {'Details: ' + str(exc) if debug else ''}"
            },
        )

    @fastapi_app.exception_handler(Exception)
    async def uncaught_exception_handler(_: Request, exc: Exception):
        return JSONResponse(
            status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
            content={
                "message": f"Internal server error.{f' Details: {str(exc)}' if debug else ''}"
            },
        )


def create_app() -> FastAPI:
    fastapi_app = FastAPI(
        title="Library API",
        docs_url="/swagger",
        root_path=settings.ROOT_PATH
    )
    setup_routing(fastapi_app)
    setup_handlers(fastapi_app, debug=settings.DEBUG)

    return fastapi_app
