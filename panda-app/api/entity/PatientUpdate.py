import datetime
from typing import Annotated, Optional

from pydantic import Field

from api.common.consts import UK_POSTCODE_REGEX
from api.entity.BaseEntity import BaseEntity


class PatientUpdate(BaseEntity):
    name: Annotated[Optional[str], Field(min_length=3)] = None
    date_of_birth: Annotated[Optional[datetime.date], Field(
        serialization_alias="dateOfBirth",
        alias="dateOfBirth"
    )] = None
    postcode: Annotated[Optional[str], Field(pattern=UK_POSTCODE_REGEX)] = None

    class Config:
        extra = "forbid"
        allow_population_by_alias = True
