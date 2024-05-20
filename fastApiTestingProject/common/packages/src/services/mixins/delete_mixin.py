from datetime import datetime
from typing import TypeVar
from uuid import UUID

from common.packages.src.core.exceptions.base import DomainException
from common.packages.src.repositories.base import BaseRepository
from common.packages.src.schemas.base import SoftDeleteSchema

RepositoryType = TypeVar("RepositoryType", bound=BaseRepository)


class DeleteMixin:
    """Class designed to delete instance from database."""

    _repository: RepositoryType = NotImplemented

    async def delete(self, uuid: UUID):
        """Delete record from database completely."""
        result = await self._repository.delete(uuid)

        return result

    async def soft_delete_wp(self, uuid: UUID, deleted_by_uuid: UUID):
        """Soft delete for objects without is_published field."""
        if not hasattr(self._repository, "soft_delete"):
            raise DomainException(f"{type(self._repository)} is not ready to apply soft delete yet.")
        soft_delete_info = SoftDeleteSchema(deleted_by=deleted_by_uuid, deleted_at=datetime.utcnow())
        result = await self._repository.soft_delete(uuid, soft_delete_info)
        return result

    async def soft_delete(self, uuid: UUID, deleted_by_uuid: UUID):
        """Apply is_deleted flag on database record."""
        if not hasattr(self._repository, "soft_delete"):
            raise DomainException(f"{type(self._repository)} is not ready to apply soft delete yet.")
        soft_delete_info = SoftDeleteSchema(deleted_by=deleted_by_uuid, deleted_at=datetime.utcnow())
        result = await self._repository.soft_delete(uuid, soft_delete_info)
        return result
