from sqlalchemy import Column, Integer, String, Date

from api.repository.model.BaseModel import BaseModel

PATIENT_TABLE_NAME = "patients"


class PatientModel(BaseModel):
    __tablename__ = PATIENT_TABLE_NAME
    id = Column(Integer, primary_key=True)
    nhs_number = Column(String(10), nullable=False, unique=True)
    name =  Column(String(100), nullable=False)
    date_of_birth = Column("dob", Date, nullable=False)
    postcode = Column(String(8), nullable=False)
