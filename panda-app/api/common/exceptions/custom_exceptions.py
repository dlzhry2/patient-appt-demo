class NotFoundException(Exception):
    def __init__(self, message: str = "Not found"):
        super().__init__(message)

class ValidationException(Exception):
    def __init__(self, message: str = "Invalid request"):
        super().__init__(message)
