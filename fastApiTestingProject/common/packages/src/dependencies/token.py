"""Token dependencies."""

from fastapi import HTTPException
from fastapi.requests import Request
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer


class JWTBearer(HTTPBearer):
    """Parse Berarer token."""

    def __init__(self, auto_error: bool = True) -> None:
        """Initialize JWT Bearer class."""
        super(JWTBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request) -> str:
        """Check auth scheme."""
        credentials: HTTPAuthorizationCredentials = await super(JWTBearer, self).__call__(request)
        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(status_code=403, detail="Invalid authentication scheme")
            return credentials.credentials
        else:
            raise HTTPException(status_code=403, detail="Invalid authorization code")
