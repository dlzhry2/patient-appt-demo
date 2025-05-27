import functools
import logging

from starlette import status
from starlette.responses import JSONResponse

from api.common.exceptions.custom_exceptions import ValidationException, NotFoundException

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def custom_exception_wrapper(func):
    @functools.wraps(func)
    async def wrapper(*args, **kwargs):
        try:
            return await func(*args, **kwargs)

        # TODO wrap the pydantic validation exceptions and ensure common response format

        except ValidationException as e:
            return JSONResponse(
                content={"message": str(e)},
                status_code=status.HTTP_400_BAD_REQUEST
            )

        except NotFoundException as e:
            return JSONResponse(
                content={"message": str(e)},
                status_code=status.HTTP_404_NOT_FOUND
            )

        except Exception as e:
            logger.error(f"Unhandled exception occurred: {e}")
            return JSONResponse(
                content={"message": "Internal Server Error"},
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    return wrapper
