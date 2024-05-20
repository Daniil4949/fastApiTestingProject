"""Auth services."""
import jwt
from fastapi import Depends
from loguru import logger

from common.packages.src.conf.settings import settings
from common.packages.src.core.exceptions.api_exception import ApiException
from common.packages.src.core.exceptions.base import DomainException
from common.packages.src.core.exceptions.error_code import DomainErrorCodeEnum
from common.packages.src.dependencies.token import JWTBearer


def decode_user_jwt(token: str, secret_key: str = settings.auth.secret_key) -> dict:
    """Decode access token."""
    try:
        payload = jwt.decode(token, secret_key, algorithms=[settings.app.algorithm])
    except jwt.ExpiredSignatureError:
        raise DomainException(
            status_code=401,
            detail="Access Token expired",
            error_code=DomainErrorCodeEnum.TOKEN_EXPIRED.value,
        )
    except jwt.exceptions.InvalidSignatureError:
        raise DomainException(
            status_code=403,
            detail="Authorization failed.",
            error_code=DomainErrorCodeEnum.AUTHORIZATION_FAILED.value,
        )
    except jwt.exceptions.DecodeError:
        raise DomainException(
            status_code=403,
            detail="Invalid access token",
            error_code=DomainErrorCodeEnum.INVALID_TOKEN.value,
        )
    return payload


class APIKeyValidator:
    @staticmethod
    def validate_russpass_api_key(api_key: str = Depends(JWTBearer())):
        """Validate external API key for russpass."""
        if api_key != settings.auth.russpass_api_key:
            raise ApiException(name="Wrong API key for Russpass client!", status_code=401)

    @staticmethod
    def validate_polylog_api_key(api_key: str = Depends(JWTBearer())):
        """Validate external API key for polylog."""
        if api_key != settings.auth.polylog_api_key:
            raise ApiException(name="Wrong API key for Polylog client!", status_code=401)


async def get_current_user(token: str = Depends(JWTBearer())) -> dict:
    """Get current user based on token."""
    payload = decode_user_jwt(token, settings.auth.secret_key)
    if payload is None:
        logger.warning("Credentials are not valid! Payload is None")
        raise ApiException(name="Credentials are not valid!", status_code=401)
    if payload.get("user_uuid") is None:
        logger.warning("Credentials are not valid! User uuid is None")
        raise ApiException(name="Credentials are not valid!", status_code=401)
    return payload


async def get_user_payload(token: str = Depends(JWTBearer())) -> dict:
    """Get user payload, based on jwt."""
    return decode_user_jwt(token)
