from typing import Optional

from pydantic import BaseModel
from typing import List


class ReadClinic(BaseModel):
    name: str
    description: str
    phone: str
    email: str
    website: Optional[str]

    class Config:
        from_attributes = True


class ClinicPagination(BaseModel):
    total: int
    page: int
    size: int
    items: List[ReadClinic]
