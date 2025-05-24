from typing import Annotated

from fastapi import APIRouter, Depends, Path
from sqlalchemy.ext.asyncio import AsyncSession

from api.common.consts import NHS_NUMBER_REGEX
from api.common.exceptions.custom_exception_wrapper import custom_exception_wrapper
from api.common.exceptions.custom_exceptions import ValidationException
from api.common.nhs_number_validator import validate_nhs_number
from api.repository.db_setup import get_db_session
from api.repository.model.Patient import Patient
from api.repository.patient_repository import PatientRepository
from api.service.patient_service import PatientService

router = APIRouter(
    prefix="/patients",
    tags=["patient"],
)

SessionDep = Annotated[AsyncSession, Depends(get_db_session)]


# TODO - Open API info such as response and errors
# Can put global errors in router object?
@router.get("/{nhs_number}")
@custom_exception_wrapper
async def get_patient(
        nhs_number: Annotated[str, Path(
            title="The NHS Number of the patient you want to retrieve",
            regex=NHS_NUMBER_REGEX,
        )],
        db_session: SessionDep
    ):
    if not validate_nhs_number(nhs_number):
        raise ValidationException("Please provide a valid NHS number")

    patient_repo = PatientRepository(db_session=db_session)
    patient_service = PatientService(repository=patient_repo)

    return await patient_service.get(nhs_number=int(nhs_number))
