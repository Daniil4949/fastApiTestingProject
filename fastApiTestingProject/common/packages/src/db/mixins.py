"""Module with mixins fields for database models."""
from datetime import datetime
from typing import Optional

from sqlalchemy import UUID, ForeignKey, func, text
from sqlalchemy.orm import Mapped, mapped_column


class UUIDMixin:
    """Identifier uuid mixin."""

    uuid: Mapped[str] = mapped_column(UUID, primary_key=True, server_default=text("gen_random_uuid()"))


class TimestampMixin:
    """Timestamp mixin."""

    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(server_default=func.now())


class UpdateMixin:
    """Update mixin."""

    updated_by: Mapped[Optional[str]] = mapped_column(ForeignKey("user.uuid"))

