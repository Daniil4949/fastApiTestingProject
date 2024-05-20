from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class SoftDeleteSchema(BaseModel):
    is_deleted: bool = True
    deleted_by: UUID
    deleted_at: datetime
