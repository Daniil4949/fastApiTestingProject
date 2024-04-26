"""Module with common query dependencies."""


class CommonQueryParams:
    """Common query param class which may be used as a dependency.

    Just use:
    commons: Annotated[CommonQueryParams, Depends(CommonQueryParams)]
    """

    def __init__(self, q: str | None = None, offset: int = 0, limit: int = 100):
        """Initialize common params."""
        self.q = q
        self.offset = offset
        self.limit = limit


class Pagination:
    """Pagination query param class which may be used as a dependency.

    Just use:
    pages: Annotated[Pagination, Depends(Pagination)]
    """

    def __init__(self, offset: int = 0, limit: int = 50):
        """Initialize common params."""
        self.offset = offset
        self.limit = limit
