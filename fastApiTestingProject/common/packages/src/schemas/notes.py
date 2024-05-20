from typing import Optional
from uuid import UUID

from pydantic import BaseModel, Field, ConfigDict


class CreateNoteSchema(BaseModel):
    title: str = Field(..., max_length=100)
    description: str = Field(..., max_length=100)
    user_id: Optional[UUID] = Field(None, exclude=True)

    model_config = ConfigDict(from_attributes=True, arbitrary_types_allowed=True)


class UpdateNoteSchema(BaseModel):
    title: Optional[str] = Field(None, max_length=100)
    description: Optional[str] = Field(None, max_length=100)
    user_id: Optional[UUID] = Field(None, exclude=True)

    model_config = ConfigDict(from_attributes=True, arbitrary_types_allowed=True)
