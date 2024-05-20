from common.packages.src.schemas.notes import CreateNoteSchema, UpdateNoteSchema
from common.packages.src.services.base import BaseCRUDService
from common.packages.src.services.mixins.delete_mixin import DeleteMixin
from notes.src.repositories.notes.core import NoteRepository


class NoteService(DeleteMixin, BaseCRUDService):
    create_scheme = CreateNoteSchema
    update_scheme = UpdateNoteSchema

    def __init__(self, repository: NoteRepository) -> None:
        """Initialize store items repository with async session."""
        super().__init__(repository)
