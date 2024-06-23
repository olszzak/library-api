from http import HTTPStatus


class LibraryApiError(Exception):
    def __init__(
        self, status_code: int, message: str = "Internal error", details: str = None
    ):
        self.status_code = status_code
        self.message = message
        self.details = details


class LibraryApiNotFound(LibraryApiError):
    def __init__(self, details: str = None):
        super().__init__(
            status_code=HTTPStatus.NOT_FOUND, message="Item not found", details=details
        )
