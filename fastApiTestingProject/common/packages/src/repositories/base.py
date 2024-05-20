"""Module with base repository realization."""

import uuid
from typing import Any, List, Sequence, TypeVar, Union

from sqlalchemy import Row, RowMapping, delete, desc, func, select, update
from sqlalchemy.ext.asyncio import AsyncSession

from common.packages.src.abstract.repository import IRepository
from common.packages.src.core.exceptions.base import DBException
from common.packages.src.core.exceptions.error_code import DBErrorCodeEnum
from common.packages.src.db.base import Base, BaseModel

TableType = TypeVar("TableType", bound=Base)
CreateBaseSchema = TypeVar("CreateBaseSchema", bound=BaseModel)
UpdateBaseSchema = TypeVar("UpdateBaseSchema", bound=BaseModel)


class BaseRepository(IRepository):
    """IRepository implementation."""

    model: TableType = None  # type: ignore
    create_scheme: CreateBaseSchema = None  # type: ignore
    update_scheme: UpdateBaseSchema = None  # type: ignore

    def __init__(self, session: AsyncSession) -> None:
        """Initialize base repository with async session."""
        self._session = session

    async def create(self, input_data: create_scheme) -> model:
        """Create model."""
        obj = self.model(**input_data.model_dump())
        self._session.add(obj)
        await self._session.flush()
        await self._session.refresh(obj)
        return obj

    async def bulk_create(self, instances_schema: List[create_scheme]) -> list[model]:
        """Bulk crate model."""
        instances = [self.model(**instance.model_dump()) for instance in instances_schema]
        self._session.add_all(instances)
        await self._session.flush()
        return instances

    @staticmethod
    def check_object(obj: model) -> Union[bool, DBException]:
        """Check if object exist."""
        if not obj:
            raise DBException(
                status_code=404,
                detail="Object not found",
                error_code=DBErrorCodeEnum.OBJECT_NOT_FOUND.value,
            )
        return True

    async def list(self, filters: Union[tuple, None] = None) -> Sequence[Row | RowMapping | Any]:
        """Get list of filtered objects."""
        query = select(self.model).order_by(self.model.created_at)
        if filters is not None:
            query.filter(*filters)
        objects = await self._session.execute(query)
        return objects.scalars().all()

    async def get_paginated(
            self, limit: int, offset: int, order_by_field: str, filters: Union[tuple, None] = None
    ) -> Sequence[Row | RowMapping | Any]:
        """Get paginated result."""

        if filters is not None:
            query = (
                select(self.model)
                .limit(limit)
                .offset(offset)
                .order_by(getattr(self.model, order_by_field, "created_at"))
                .filter(*filters)
            )
        else:
            query = (
                select(self.model)
                .limit(limit)
                .offset(offset)
                .order_by(getattr(self.model, order_by_field, "created_at"))
            )
        objects = await self._session.execute(query)
        return objects.scalars().all()

    async def retrieve(self, pk: uuid.UUID) -> Union[model, DBException]:
        """Get object by primary key."""
        res = await self._session.execute(select(self.model).where(self.model.uuid == pk))
        obj = res.scalars().first()
        self.check_object(obj)
        await self._session.refresh(obj)
        return obj

    async def bulk_retrieve(self, pks: List[uuid.UUID]) -> List[model] or DBException:
        """Get object by primary key."""
        query = select(self.model).where(self.model.uuid.in_(pks))
        res = await self._session.execute(query)
        objs = res.scalars().all()
        [self.check_object(obj) for obj in objs]
        [await self._session.refresh(obj) for obj in objs]
        return objs

    async def update(
            self, pk: uuid.UUID, input_data: update_scheme, partial: bool = False
    ) -> Union[model, DBException]:
        """Update object by specified primary key."""
        values_dump_data = input_data.model_dump(exclude_unset=partial)
        if values_dump_data:
            updated_obj = await self._session.execute(
                update(self.model)
                .where(self.model.uuid == pk)
                .values(**values_dump_data)
                .returning(self.model)
            )
            await self._session.flush()
            res = updated_obj.scalars().first()
            if res is None:
                raise DBException(
                    "Object Not Found",
                    status_code=404,
                    error_code=DBErrorCodeEnum.OBJECT_NOT_FOUND.value,
                )
            await self._session.refresh(res)
            return res
        else:
            return await self._session.get(self.model, pk)

    async def bulk_update(
            self, pks: List[uuid.UUID], input_data: update_scheme, partial: bool = False
    ) -> List[model] or DBException:
        """Update object by specified primary key."""
        retrieved_objs = await self.bulk_retrieve(pks)
        await self._session.execute(
            update(self.model).where(self.model.uuid.in_(pks)).values(**input_data.dict(exclude_unset=partial))
        )
        return retrieved_objs

    async def delete(self, pk: uuid.UUID) -> dict:
        """Delete object by specified primary key."""
        res = await self._session.execute(delete(self.model).where(self.model.uuid == pk))
        await self._session.flush()

        return {"affected_rows": res.rowcount}

    async def delete_all(self) -> dict:
        """Delete all objects of model."""
        res = await self._session.execute(delete(self.model))
        return {"affected_rows": res.rowcount}

    async def get_first_by_filter(self, filters: dict) -> model:
        """Get first appropriate object which meets filters."""
        query = select(self.model).filter_by(**filters)
        res = await self._session.execute(query)
        return res.scalars().first()

    async def get_last_by_filter(self, filters: dict) -> model:
        """Get last appropriate object which meets filters."""
        res = await self._session.execute(select(self.model).filter_by(**filters).order_by(desc("created_at")))
        return res.scalars().first()

    async def get_or_create(self, input_data: create_scheme) -> model:
        """Get object if exists otherwise create new one."""
        res = await self.get_first_by_filter(input_data.model_dump())
        if res:
            return res
        return await self.create(input_data)

    async def get_by_uuids(self, uuids: [int]) -> Sequence[Row | RowMapping | Any]:
        """Get by uuids."""
        query = select(
            [self.model],
            self.model.uuid.in_(uuids),
        )
        res = await self._session.execute(query)
        return res.scalars().all()

    async def update_with_dict(self, pk: uuid.UUID, input_data: dict) -> Union[model, DBException]:
        """Update object by specified primary key."""
        retrieved_obj = await self.retrieve(pk)
        await self._session.execute(update(self.model).where(self.model.uuid == pk).values(**input_data))
        await self._session.flush()
        return retrieved_obj

