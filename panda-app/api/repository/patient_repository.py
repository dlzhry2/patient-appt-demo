from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from api.common.exceptions.custom_exceptions import NotFoundException
from api.entity.Patient import Patient
from api.mapper.patient_mapper import PatientMapper
from api.repository.base_repository import BaseRepository
from api.repository.model.PatientModel import PatientModel


class PatientRepository(BaseRepository):
    def __init__(self, db_session: AsyncSession):
        super().__init__(db_session)
        self.mapper = PatientMapper()

    async def create(self, patient: Patient) -> None:
        self.db_session.add(
            self.mapper.to_model(patient)
        )
        await self.db_session.commit()

    async def delete(self, nhs_number: str) -> None:
        patient_model = await self._get_by_nhs_number(nhs_number)

        await self.db_session.delete(patient_model)
        await self.db_session.commit()

    async def get(self, nhs_number: str) -> Patient | None:
        patient_model = await self._get_by_nhs_number(nhs_number)

        if not patient_model:
            return None

        return self.mapper.to_entity(patient_model)

    async def update(self, nhs_number: str, updates: dict) -> Patient:
        patient_model = await self._get_by_nhs_number(nhs_number)

        if not patient_model:
            raise NotFoundException()

        for key, value in updates.items():
            setattr(patient_model, key, value)

        await self.db_session.commit()
        return self.mapper.to_entity(patient_model)

    async def _get_by_nhs_number(self, nhs_number: str) -> PatientModel | None:
        result = await self.db_session.execute(
            select(PatientModel).where(PatientModel.nhs_number == nhs_number)
        )
        return result.scalar_one_or_none()
