from sqlalchemy import Column, Integer, String

from api.repository.model.Base import Base

PATIENT_TABLE_NAME = "patients"


class Patient(Base):
    __tablename__ = PATIENT_TABLE_NAME
    nhs_number = Column("nhsnumber", Integer, primary_key=True)
    name =  Column(String(100), nullable=False)
