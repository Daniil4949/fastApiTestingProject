"""Soft Delete Mixin."""
from uuid import UUID

from sqlalchemy import delete, update

from common.packages.src.core.exceptions.base import DBException
from common.packages.src.core.exceptions.error_code import DBErrorCodeEnum
from common.packages.src.schemas.base import SoftDeleteSchema


class DeleteMixin:
    """Soft Delete mixin class."""

    _session = NotImplemented
    model = NotImplemented
    soft_delete_schema = SoftDeleteSchema

    async def delete(self, uuid: UUID):
        """Delete record from database completely."""
        stmt = delete(self.model).where(self.model.uuid == uuid)

        res = await self._session.execute(stmt)
        await self._session.flush()

        return {"affected_rows": res.rowcount}

    async def soft_delete(self, uuid: UUID, input_data: soft_delete_schema):
        """Soft delete method."""
        if any(
                (
                        not hasattr(self.model, "deleted_at"),
                        not hasattr(self.model, "deleted_by"),
                        not hasattr(self.model, "is_deleted"),
                )
        ):
            raise DBException(
                "Model has no soft-delete-specific fields.",
                status_code=500,
                error_code=DBErrorCodeEnum.DB_FIELD_NOT_FOUND,
            )

        stmt = update(self.model).where(self.model.uuid == uuid).values(**input_data.model_dump()).returning(self.model)

        obj = await self._session.execute(stmt)
        await self._session.flush()
        result = obj.scalars().first()

        if result is None:
            raise DBException(
                "Object Not Found",
                status_code=404,
                error_code=DBErrorCodeEnum.OBJECT_NOT_FOUND,
            )
        return result
