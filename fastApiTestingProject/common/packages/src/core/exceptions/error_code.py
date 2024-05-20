import enum


class DomainErrorCodeEnum(enum.StrEnum):
    INVALID_TOKEN = "invalid_token"
    TOKEN_EXPIRED = "expired_token"
    TOKEN_INVALID_OR_EXPIRED = "token_invalid_or_expired"
    WRONG_PASSWORD_PROVIDED = "wrong_password_provided"
    AUTHORIZATION_FAILED = "authorization_failed"


class AuthorizationErrorCodeEnum(enum.StrEnum):
    USER_NOT_VERIFIED = "user_not_verified"


class DBErrorCodeEnum(enum.StrEnum):
    INVALID_CREDENTIALS = "invalid_credentials"
    USER_NOT_FOUND = "user_not_found"
    USER_DOES_NOT_EXISTS = "user_does_not_exists"
    OBJECT_NOT_FOUND = "object_not_found"
    DB_FIELD_NOT_FOUND = "database_field_not_found"
