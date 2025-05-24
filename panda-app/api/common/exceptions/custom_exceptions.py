from starlette import status


class PandaBaseException(Exception):
    def __init__(self, message: str, status_code: int):
        super().__init__(message)
        self.status_code = status_code

class NotFoundException(PandaBaseException):
    def __init__(self, message: str = "Not found", status_code: int = status.HTTP_404_NOT_FOUND):
        super().__init__(message, status_code)

class ValidationException(PandaBaseException):
    def __init__(self, message: str = "Invalid request", status_code: int = status.HTTP_400_BAD_REQUEST):
        super().__init__(message, status_code)
