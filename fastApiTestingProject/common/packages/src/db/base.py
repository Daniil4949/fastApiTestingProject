"""Base database model classes."""
from typing import Any

from sqlalchemy import JSON, inspect
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    """Inherit from Declarative base."""

    type_annotation_map = {
        dict[str, Any]: JSON
    }


class BaseModel(Base):
    """Base database model definition."""

    __abstract__ = True

    def as_dict(self) -> dict:
        """Serialize any model to python dictionary."""
        return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}
