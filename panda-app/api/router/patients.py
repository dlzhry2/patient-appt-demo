from typing import Annotated

from fastapi import APIRouter, Depends, Path, status
from sqlalchemy.ext.asyncio import AsyncSession

from api.common.consts import NHS_NUMBER_REGEX
from api.common.exceptions.custom_exception_wrapper import custom_exception_wrapper
from api.common.exceptions.custom_exceptions import ValidationException
from api.common.nhs_number_validator import validate_nhs_number
from api.entity.Patient import Patient
from api.entity.PatientUpdate import PatientUpdate
from api.repository.db_setup import get_db_session
from api.repository.patient_repository import PatientRepository
from api.service.patient_service import PatientService

router = APIRouter(
    prefix="/patients",
    tags=["patient"],
)

SessionDep = Annotated[AsyncSession, Depends(get_db_session)]


@router.post("", status_code=status.HTTP_201_CREATED)
@custom_exception_wrapper
async def create(patient: Patient, db_session: SessionDep) -> Patient:
    patient_repo = PatientRepository(db_session=db_session)
    patient_service = PatientService(repository=patient_repo)
    await patient_service.create(patient)

    return patient


@router.delete("/{nhs_number}", status_code=status.HTTP_204_NO_CONTENT)
@custom_exception_wrapper
async def delete(
        nhs_number: Annotated[str, Path(
            title="The NHS Number of the patient you want to retrieve",
            regex=NHS_NUMBER_REGEX,
        )],
        db_session: SessionDep
) -> None:
    if not validate_nhs_number(nhs_number):
        raise ValidationException("Please provide a valid NHS number")

    patient_repo = PatientRepository(db_session=db_session)
    patient_service = PatientService(repository=patient_repo)
    await patient_service.delete(nhs_number)


@router.get("/{nhs_number}")
@custom_exception_wrapper
async def get(
        nhs_number: Annotated[str, Path(
            title="The NHS Number of the patient you want to retrieve",
            regex=NHS_NUMBER_REGEX,
        )],
        db_session: SessionDep
) -> Patient:
    if not validate_nhs_number(nhs_number):
        raise ValidationException("Please provide a valid NHS number")

    patient_repo = PatientRepository(db_session=db_session)
    patient_service = PatientService(repository=patient_repo)

    return await patient_service.get(nhs_number=nhs_number)


@router.patch("/{nhs_number}")
@custom_exception_wrapper
async def update(
        nhs_number: Annotated[str, Path(
            title="The NHS Number of the patient you want to retrieve",
            regex=NHS_NUMBER_REGEX,
        )],
        patient_update: PatientUpdate,
        db_session: SessionDep
) -> Patient:
    if not validate_nhs_number(nhs_number):
        raise ValidationException("Please provide a valid NHS number")

    updates_dict = patient_update.model_dump(exclude_unset=True)

    if not updates_dict:
        raise ValidationException("Please provide at least one updated field")

    patient_repo = PatientRepository(db_session=db_session)
    patient_service = PatientService(repository=patient_repo)

    return await patient_service.update(nhs_number=nhs_number, updates=updates_dict)
