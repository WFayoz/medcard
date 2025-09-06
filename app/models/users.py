import enum

from sqlalchemy import String, Enum
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base_model import Base


class User(Base):
    class Role(enum.Enum):
        ADMIN = 'admin', 'Admin',
        PATIENT = 'patient', 'Patient',
        MED_OWNER = 'med_owner', 'Med_owner',
        DOCTOR = 'doctor', 'Doctor'

    firstname : Mapped[str] = mapped_column(String(255))
    lastname : Mapped[str] = mapped_column(String(255))
    phone_number : Mapped[str] = mapped_column(String(255))
    role : Mapped[str] = mapped_column(Enum(Role))