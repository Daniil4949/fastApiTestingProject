import typing as t
from http import HTTPStatus

from fastapi import HTTPException


class ApiException(HTTPException):
    def __init__(self, name: t.Union[str, dict], status_code: t.Union[HTTPStatus, int] = HTTPStatus.BAD_REQUEST):
        self.name = name
        self.status_code = status_code if status_code else HTTPStatus.BAD_REQUEST