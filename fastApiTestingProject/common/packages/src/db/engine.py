"""Module with database engine setup function."""
from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine


def get_engine(db_uri: str, echo: bool = False) -> AsyncEngine:
    """Create database engine."""
    return create_async_engine(
        db_uri,
        pool_use_lifo=True,
        pool_pre_ping=True,
        pool_recycle=3600,
        pool_size=10,
        echo=echo,
    )