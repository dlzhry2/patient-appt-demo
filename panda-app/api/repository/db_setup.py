import contextlib
import os
from typing import AsyncIterator

from sqlalchemy import URL
from sqlalchemy.ext.asyncio import (
    AsyncConnection,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

def get_connection_url() -> URL:
    host = os.getenv("DB_HOST") if os.getenv("DB_HOST") is not None else "localhost"

    return URL.create(
        "postgresql+asyncpg",
        username=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=host,
        database=os.getenv("DB_NAME")
    )

class DatabaseSessionManager:
    def __init__(self, host: URL):
        self._engine = create_async_engine(host)
        self._session_maker = async_sessionmaker(autocommit=False, bind=self._engine, expire_on_commit=False)

    async def close(self):
        if self._engine is None:
            raise Exception("DatabaseSessionManager is not initialized")
        await self._engine.dispose()

        self._engine = None
        self._session_maker = None

    @contextlib.asynccontextmanager
    async def connect(self) -> AsyncIterator[AsyncConnection]:
        if self._engine is None:
            raise Exception("DatabaseSessionManager is not initialized")

        async with self._engine.begin() as connection:
            try:
                yield connection
            except Exception:
                await connection.rollback()
                raise

    @contextlib.asynccontextmanager
    async def session(self) -> AsyncIterator[AsyncSession]:
        if self._session_maker is None:
            raise Exception("DatabaseSessionManager is not initialized")

        session = self._session_maker()
        try:
            yield session
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()


sessionmanager = DatabaseSessionManager(get_connection_url())


async def get_db_session():
    async with sessionmanager.session() as session:
        yield session
