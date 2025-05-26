from api.common.consts import POSTCODE_FIELD_NAME
from api.common.exceptions.custom_exceptions import NotFoundException, ValidationException
from api.common.postcode_formatter import format_postcode
from api.entity.Patient import Patient
from api.repository.patient_repository import PatientRepository
from api.service.base_service import BaseService


class PatientService(BaseService):
    def __init__(self, repository: PatientRepository):
        super().__init__(repository)

    async def create(self, patient: Patient) -> None:
        patient_exists = await self._patient_exists(patient.nhs_number)

        if patient_exists:
            raise ValidationException("Patient already exists")

        await self.repository.create(patient)

    async def delete(self, nhs_number: str) -> None:
        patient = await self.repository.get(nhs_number)

        if not patient:
            raise NotFoundException()

        await self.repository.delete(nhs_number)

    async def get(self, nhs_number: str) -> Patient:
        patient = await self.repository.get(nhs_number)

        if not patient:
            raise NotFoundException()

        return patient

    async def update(self, nhs_number: str, updates: dict) -> Patient:
        patient = await self.repository.get(nhs_number)

        if not patient:
            raise NotFoundException()

        if POSTCODE_FIELD_NAME in updates:
            updates[POSTCODE_FIELD_NAME] = format_postcode(updates[POSTCODE_FIELD_NAME])

        return await self.repository.update(nhs_number, updates)

    async def _patient_exists(self, nhs_number: str) -> bool:
        return await self.repository.get(nhs_number) is not None
