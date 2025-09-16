import enum

from sqlalchemy import String, Enum
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base_model import Model


class User(Model):
    class Role(enum.Enum):
        ADMIN = 'ADMIN'
        PATIENT = 'PATIENT'
        MED_OWNER = 'MED_OWNER'
        DOCTOR = 'DOCTOR'

    firstname: Mapped[str] = mapped_column(String(255))
    lastname: Mapped[str] = mapped_column(String(255))
    phone_number: Mapped[str] = mapped_column(String(255))
    password: Mapped[str] = mapped_column(String(255))
    role: Mapped[str] = mapped_column(Enum(Role, name='role'))
