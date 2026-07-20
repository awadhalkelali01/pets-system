from datetime import date

from sqlalchemy import Date
from sqlalchemy import ForeignKey
from sqlalchemy import Numeric
from sqlalchemy import String
from sqlalchemy import Text

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from .base import Base
from .base import UUIDMixin
from .base import TimestampMixin


class PurchaseOrder(UUIDMixin, TimestampMixin, Base):

    __tablename__ = "purchase_orders"

    po_number: Mapped[str] = mapped_column(
        String(50),
        unique=True
    )

    po_date: Mapped[date] = mapped_column(
        Date,
        nullable=True
    )

    currency: Mapped[str] = mapped_column(
        String(10),
        nullable=True
    )

    total_amount: Mapped[float] = mapped_column(
        Numeric(18,2),
        nullable=True
    )

    warehouse: Mapped[str] = mapped_column(
        String(100),
        nullable=True
    )

    received_date: Mapped[date] = mapped_column(
        Date,
        nullable=True
    )

    remarks: Mapped[str] = mapped_column(
        Text,
        nullable=True
    )

    vendor_id = mapped_column(
        ForeignKey("vendors.id")
    )

    vendor = relationship(
        "Vendor",
        back_populates="purchase_orders"
    )

    items = relationship(
        "PurchaseOrderItem",
        back_populates="purchase_order",
        cascade="all, delete-orphan"
    )

    ncrfis = relationship(
        "NCRFI",
        back_populates="purchase_order"
    )
