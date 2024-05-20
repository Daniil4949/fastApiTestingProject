class BaseAppException(Exception):
    """Custom base app exception."""

    DEFAULT_STATUS_CODE = 500
    DEFAULT_ERROR_MESSAGE = "Unexpected error occurred"
    DEFAULT_ERROR_CODE = "unexpected_error"

    def __init__(
            self,
            detail: str | None = None,
            status_code: int | None = None,
            error_code: str | None = None,
    ) -> None:
        """Initialize exception details."""
        self.status_code = status_code or self.DEFAULT_STATUS_CODE
        self.detail = detail or self.DEFAULT_ERROR_MESSAGE
        self.error_code = error_code or self.DEFAULT_ERROR_CODE


class InfrastructureException(BaseAppException):
    """Custom Infra exception."""

    DEFAULT_MESSAGE = "Infrastructure exception occurred"
    DEFAULT_ERROR_CODE = "infrastructure_exception"


class DBException(InfrastructureException):
    """Custom DB exception."""

    DEFAULT_MESSAGE = "Database exception occurred"
    DEFAULT_STATUS_CODE = 404
    DEFAULT_ERROR_CODE = "db_exception"


class DomainException(BaseAppException):
    """Custom domain exception."""

    DEFAULT_ERROR_MESSAGE = "Domain exception occurred"
    DEFAULT_STATUS_CODE = 400
    DEFAULT_ERROR_CODE = "domain_exception"
