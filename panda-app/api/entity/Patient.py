import datetime
from typing import Annotated

from pydantic import Field, field_validator

from api.common.consts import NHS_NUMBER_REGEX, UK_POSTCODE_REGEX
from api.common.nhs_number_validator import validate_nhs_number
from api.entity.BaseEntity import BaseEntity


class Patient(BaseEntity):
    nhs_number: Annotated[str, Field(
        serialization_alias="nhsNumber",
        pattern=NHS_NUMBER_REGEX
    )]
    # TODO - align naming to GDS guidelines
    name: Annotated[str, Field(min_length=3)]
    date_of_birth: Annotated[datetime.date, Field(serialization_alias="dateOfBirth")]
    postcode: Annotated[str, Field(pattern=UK_POSTCODE_REGEX)]

    @field_validator('nhs_number')
    def nhs_number_is_valid(cls, v: str) -> str:
        if not validate_nhs_number(v):
            raise ValueError("Invalid NHS number")

        return v
