from sqlalchemy.ext.asyncio import AsyncSession

from notes.src.repositories.notes.core import NoteRepository
from notes.src.services.core import NoteService


def provide_notes_service(session: AsyncSession) -> NoteService:
    notes_repository = NoteRepository(session)
    notes_service = NoteService(notes_repository)
    return notes_service
