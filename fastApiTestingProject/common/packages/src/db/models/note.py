from typing import TYPE_CHECKING

from sqlalchemy import UUID, ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from common.packages.src.db.base import BaseModel
from common.packages.src.db.mixins import TimestampMixin, UUIDMixin

if TYPE_CHECKING:
    from common.packages.src.db.models import User


class Note(BaseModel, UUIDMixin, TimestampMixin):
    """Model definition."""

    __tablename__ = "store_item"

    title: Mapped[str] = mapped_column(String(100))
    description: Mapped[str] = mapped_column(Text)
    user_id: Mapped[str | None] = mapped_column(UUID, ForeignKey("user.uuid"))
    user: Mapped["User"] = relationship(foreign_keys="Note.user_id", lazy="selectin")

