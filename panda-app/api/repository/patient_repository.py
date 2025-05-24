from api.repository.base_repository import BaseRepository
from api.repository.model.Patient import Patient


class PatientRepository(BaseRepository):
    async def get(self, nhs_number: int) -> Patient | None:
        return await self.db_session.get(Patient, nhs_number)
