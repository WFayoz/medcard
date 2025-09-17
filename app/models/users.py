import enum

from sqlalchemy import String, Enum, select
from sqlalchemy.orm import Mapped, mapped_column
from app.models.base_model import Model, db


class User(Model):
    class Role(enum.Enum):
        ADMIN = 'ADMIN'
        PATIENT = 'PATIENT'
        MED_OWNER = 'MED_OWNER'
        DOCTOR = 'DOCTOR'

    firstname: Mapped[str] = mapped_column(String(255))
    lastname: Mapped[str] = mapped_column(String(255))
    phone_number: Mapped[str] = mapped_column(String(255))  # TODO unique
    role: Mapped[str] = mapped_column(Enum(Role, name='role'), default=Role.PATIENT)
    # TODO specialist
    # email: Mapped[EmailStr] = mapped_column(String(150), nullable=True, unique=True)
    password: Mapped[str] = mapped_column(String(500), nullable=True)

    # TODO M2M doctor <-> clinics
    @classmethod
    async def get_by_phone(cls, phone_number: str):
        result = await db.execute(select(cls).where(cls.phone_number == phone_number))
        return result.scalar_one_or_none()
