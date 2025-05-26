from typing import Annotated

from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from api.router import patients
from api.repository.db_setup import get_db_session

SessionDep = Annotated[AsyncSession, Depends(get_db_session)]

app = FastAPI()
app.include_router(patients.router)
