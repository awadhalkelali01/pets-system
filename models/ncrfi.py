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


class NCRFI(UUIDMixin, TimestampMixin, Base):

    __tablename__ = "ncrfis"

    ncrfi_number: Mapped[str] = mapped_column(
        String(80),
        unique=True
    )

    invoice_number: Mapped[str] = mapped_column(
        String(100),
        nullable=True
    )

    amount = mapped_column(
        Numeric(18,2),
        nullable=True
    )

    currency: Mapped[str] = mapped_column(
        String(10),
        nullable=True
    )

    approval_date: Mapped[date] = mapped_column(
        Date,
        nullable=True
    )

    remarks: Mapped[str] = mapped_column(
        Text,
        nullable=True
    )

    purchase_order_id = mapped_column(
        ForeignKey("purchase_orders.id")
    )

    purchase_order = relationship(
        "PurchaseOrder",
        back_populates="ncrfis"
    )
