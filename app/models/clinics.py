from sqlalchemy import String
from sqlalchemy.orm import mapped_column, Mapped

from app.models.base_model import Model


class Clinic(Model):
    name: Mapped[str] = mapped_column(unique=True)
    phone: Mapped[str] = mapped_column(String(15), unique=True)
    email: Mapped[str] = mapped_column(String, unique=True)
    website: Mapped[str] = mapped_column(String, unique=True)
    location: Mapped[str] = mapped_column(String(255))
    # medowner_id : Mapped[str] = mapped_column(ForeignKey('user.id'), unique=True)
    # medowner = relationship('User', foreign_keys=[medowner_id])
