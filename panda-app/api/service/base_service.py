from api.repository.patient_repository import PatientRepository


class BaseService:
    def __init__(self, repository: PatientRepository):
        self.repository = repository
