from pydantic import EmailStr
from sqlalchemy import String, Float, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship

from app.models.base_model import Model


class Clinic(Model):
    name: Mapped[str] = mapped_column(String(255))
    phone: Mapped[str] = mapped_column(String(15))
    email: Mapped[EmailStr] = mapped_column(String(255))
    website: Mapped[str] = mapped_column(String(510), nullable=True)
    lat: Mapped[float] = mapped_column(Float)
    lng: Mapped[float] = mapped_column(Float)
    parent_id: Mapped[str] = mapped_column(ForeignKey('clinics.id', ondelete='CASCADE'), nullable=True)
    parent: Mapped['Clinic'] = relationship(
        'Clinic',
        remote_side='Clinic.id',
        back_populates='branches',
    )
    branches: Mapped[list['Clinic']] = relationship(
        'Clinic',
        back_populates='parent',
        cascade='all, delete, delete-orphan',
    )
    # medowner_id : Mapped[str] = mapped_column(ForeignKey('user.id'), unique=True)
    # medowner = relationship('User', foreign_keys=[medowner_id])
