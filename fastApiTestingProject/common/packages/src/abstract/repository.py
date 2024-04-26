"""Module with repository interface."""
from abc import ABC, abstractmethod
from typing import Any


class IRepository(ABC):
    """Repository interface class."""

    @abstractmethod
    async def retrieve(self, *args: Any, **kwargs: Any) -> Any:
        """Get data from database."""
        raise NotImplementedError("Implement get_by_id method")

    @abstractmethod
    async def create(self, *args: Any, **kwargs: Any) -> Any:
        """Add new data to database."""
        raise NotImplementedError("Implement create method")

    @abstractmethod
    async def update(self, *args: Any, **kwargs: Any) -> Any:
        """Update specified data in database."""
        raise NotImplementedError("Implement update method")

    @abstractmethod
    async def delete(self, *args: Any, **kwargs: Any) -> Any:
        """Delete specified data from database."""
        raise NotImplementedError("Implement remove method")
