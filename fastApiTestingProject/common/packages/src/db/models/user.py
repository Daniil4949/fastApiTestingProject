from typing import Optional

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from common.packages.src.db import BaseModel, TimestampMixin, UUIDMixin


class User(BaseModel, UUIDMixin, TimestampMixin):
    """Model definition."""

    __tablename__ = "user"

    name: Mapped[Optional[str]] = mapped_column(String(50))
    surname: Mapped[Optional[str]] = mapped_column(String(50))
    email: Mapped[str] = mapped_column(String(255))
    password: Mapped[str] = mapped_column(String(255))
