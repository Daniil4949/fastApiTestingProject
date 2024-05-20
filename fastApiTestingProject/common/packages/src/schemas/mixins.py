from datetime import datetime
from uuid import UUID


class DeletableMixin:
    """Deletable Mixin."""

    is_deleted: bool = False
    deleted_at: datetime | UUID | None = None
    deleted_by: str | UUID | None = None


class UpdateMixin:
    """Update mixin."""

    updated_by: str | UUID | None = None
