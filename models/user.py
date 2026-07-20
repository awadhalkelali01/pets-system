from sqlalchemy import Boolean
from sqlalchemy import ForeignKey
from sqlalchemy import String

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from .base import Base
from .base import UUIDMixin
from .base import TimestampMixin


class User(UUIDMixin, TimestampMixin, Base):

    __tablename__ = "users"

    full_name: Mapped[str] = mapped_column(
        String(120)
    )

    email: Mapped[str] = mapped_column(
        String(120),
        unique=True
    )

    password_hash: Mapped[str] = mapped_column(
        String(255)
    )

    active: Mapped[bool] = mapped_column(
        Boolean,
        default=True
    )

    role_id = mapped_column(
        ForeignKey("roles.id")
    )

    role = relationship(
        "Role",
        back_populates="users"
    )
