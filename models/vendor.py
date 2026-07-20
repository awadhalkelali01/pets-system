from sqlalchemy import String

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from .base import Base
from .base import UUIDMixin
from .base import TimestampMixin


class Vendor(UUIDMixin, TimestampMixin, Base):

    __tablename__ = "vendors"

    vendor_code: Mapped[str] = mapped_column(
        String(50),
        unique=True
    )

    vendor_name: Mapped[str] = mapped_column(
        String(200)
    )

    country: Mapped[str] = mapped_column(
        String(100),
        nullable=True
    )

    purchase_orders = relationship(
        "PurchaseOrder",
        back_populates="vendor"
    )
