"""Module with CRUD Service interface."""
from abc import ABC, abstractmethod
from typing import Any


class ICRUDService(ABC):
    """CRUD Service interface."""

    @abstractmethod
    async def get_by_uuid(self, *args, **kwargs) -> Any:
        """Get obj by uuid."""
        raise NotImplementedError("Implement get_by_uuid method")

    @abstractmethod
    async def create(self, *args, **kwargs) -> Any:
        """Create obj."""
        raise NotImplementedError("Implement create method")

    @abstractmethod
    async def update(self, *args, **kwargs) -> Any:
        """Update obj."""
        raise NotImplementedError("Implement update method")

    @abstractmethod
    async def delete_by_uuid(self, *args, **kwargs) -> Any:
        """Delete obj by uuid."""
        raise NotImplementedError("Implement delete_by_uuid method")
