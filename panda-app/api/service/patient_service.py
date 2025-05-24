from api.common.exceptions.custom_exceptions import NotFoundException
from api.repository.model.Patient import Patient
from api.service.base_service import BaseService


class PatientService(BaseService):
    async def get(self, nhs_number: int) -> Patient:
        # TODO - need to do some mapping? e.g. localise timestamp
        patient = await self.repository.get(nhs_number)

        if not patient:
            raise NotFoundException()

        return patient
