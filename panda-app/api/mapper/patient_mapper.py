from api.common.postcode_formatter import format_postcode
from api.entity.Patient import Patient
from api.repository.model.PatientModel import PatientModel


class PatientMapper:
    @staticmethod
    def to_model(entity: Patient) -> PatientModel:
        model = PatientModel()
        model.nhs_number = entity.nhs_number
        model.name = entity.name
        model.date_of_birth = entity.date_of_birth
        model.postcode = format_postcode(entity.postcode)

        return model

    @staticmethod
    def to_entity(model: PatientModel) -> Patient:
        return Patient(
            nhs_number=model.nhs_number,
            name=model.name,
            date_of_birth=model.date_of_birth,
            postcode=model.postcode,
        )
