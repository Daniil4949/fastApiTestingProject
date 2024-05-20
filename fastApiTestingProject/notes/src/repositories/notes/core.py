from sqlalchemy.ext.asyncio import AsyncSession

from common.packages.src.repositories.base import BaseRepository
from common.packages.src.repositories.mixins.delete_mixin import DeleteMixin

from common.packages.src.db.models import Note
from common.packages.src.schemas.notes import CreateNoteSchema, UpdateNoteSchema


class NoteRepository(DeleteMixin, BaseRepository):
    model = Note
    create_scheme = CreateNoteSchema
    update_scheme = UpdateNoteSchema

    def __init__(self, session: AsyncSession):
        """Initialize store items repository with async session."""
        super().__init__(session)
