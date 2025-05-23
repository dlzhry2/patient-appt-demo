from typing import Annotated

from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from api.repository.db_setup import get_db_session
from api.repository.model.Patient import Patient

SessionDep = Annotated[AsyncSession, Depends(get_db_session)]

app = FastAPI()

@app.get("/patients/{nhs_number}")
async def get_patient(nhs_number: str, db_session: SessionDep):
    patient = await db_session.get(Patient, int(nhs_number))

    return patient
