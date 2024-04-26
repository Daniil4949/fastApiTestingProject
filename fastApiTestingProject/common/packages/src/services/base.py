"""Base CRUD Service realizations."""
import uuid as _uuid
from typing import TypeVar

from common.packages.src.abstract.repository import IRepository
from common.packages.src.abstract.service import ICRUDService
from common.packages.src.db.base import BaseModel

ServiceRepository = TypeVar("ServiceRepository", bound=IRepository)
CreateBaseSchema = TypeVar("CreateBaseSchema", bound=BaseModel)
UpdateBaseSchema = TypeVar("UpdateBaseSchema", bound=BaseModel)


class BaseCRUDService(ICRUDService):
    """Base CRUD Service realization."""

    create_scheme: CreateBaseSchema = None  # type: ignore
    update_scheme: UpdateBaseSchema = None  # type: ignore

    def __init__(self, repository: ServiceRepository) -> None:
        """Init method of base crud service class."""
        self._repository = repository

    async def get_by_uuid(self, uuid: _uuid.UUID):
        """Get obj by uuid."""
        obj = await self._repository.retrieve(uuid)
        return obj

    async def get_all(self):
        """Get all objects."""
        objs = await self._repository.list()
        return objs

    async def get_paginated(self, limit: int, offset: int):
        """Get paginated result."""
        objs = await self._repository.get_paginated(limit=limit, offset=offset)

    async def create(self, data: create_scheme):
        """Create obj."""
        obj = await self._repository.create(data)
        return obj

    async def update(self, uuid: _uuid.UUID, data: update_scheme):
        """Update by uuid."""
        result = await self._repository.update(uuid, data)
        return result

    async def partial_update(self, uuid: _uuid.UUID, data: update_scheme):
        """Partial update by uuid."""
        result = await self._repository.update(uuid, data, partial=True)
        return result

    async def delete_by_uuid(self, uuid: _uuid.UUID) -> dict:
        """Delete obj by uuid."""
        result = await self._repository.delete(uuid)
        return result
