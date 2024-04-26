"""Module with session setup and its context manager."""
from contextlib import asynccontextmanager
from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import async_sessionmaker

from common.packages.src.conf.settings import settings
from common.packages.src.db.engine import get_engine


@asynccontextmanager
async def get_async_session(
        db_connection_string: str = settings.postgres.db_uri,
        echo: bool = settings.postgres.echo
) -> AsyncGenerator:
    """Session context manager, catches all errors."""
    if not db_connection_string:
        raise TypeError("DBSession: No connection string set")

    async_sql_session = async_sessionmaker(
        bind=get_engine(db_connection_string, echo), expire_on_commit=False
    )
    async_db_session = async_sql_session()

    try:
        yield async_db_session
        await async_db_session.commit()
    except Exception:
        await async_db_session.rollback()
        raise
    finally:
        await async_db_session.close()