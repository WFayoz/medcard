from typing import TypeVar, Generic

from pydantic import BaseModel

from app.schemas.clinics import ReadClinic

T = TypeVar('T', bound=BaseModel)


class ResponseSchema(BaseModel, Generic[T]):
    message: str
    data: T | None = None


__all__ = [
    'ResponseSchema',
    'ReadClinic',
]
