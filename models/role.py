from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from .base import Base
from .base import UUIDMixin
from .base import TimestampMixin


class Role(UUIDMixin, TimestampMixin, Base):

    __tablename__ = "roles"

    name: Mapped[str] = mapped_column(
        String(50),
        unique=True
    )

    description: Mapped[str] = mapped_column(
        String(200)
    )

    users = relationship(
        "User",
        back_populates="role"
    )
