from sqlalchemy import Column, Integer, String, Date

from api.repository.model.Base import Base

PATIENT_TABLE_NAME = "patients"


class Patient(Base):
    __tablename__ = PATIENT_TABLE_NAME
    nhs_number = Column(Integer, primary_key=True)
    name =  Column(String(100), nullable=False)
    date_of_birth = Column("dob", Date, nullable=False)
    postcode = Column(String(8), nullable=False)
