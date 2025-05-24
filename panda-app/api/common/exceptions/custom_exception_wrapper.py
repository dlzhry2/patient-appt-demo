import functools
import logging

from starlette import status
from starlette.responses import JSONResponse

from api.common.exceptions.custom_exceptions import PandaBaseException

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def custom_exception_wrapper(func):
    @functools.wraps(func)
    async def wrapper(*args, **kwargs):
        try:
            return await func(*args, **kwargs)

        # TODO wrap the pydantic validation exceptions

        except PandaBaseException as e:
            return JSONResponse(
                content={"message": str(e)},
                status_code=e.status_code
            )

        except Exception as e:
            logger.error(f"Unhandled exception occurred: {e}")
            return JSONResponse(
                content={"message": "Internal Server Error"},
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    return wrapper
