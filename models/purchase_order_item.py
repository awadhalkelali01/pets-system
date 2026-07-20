from sqlalchemy import ForeignKey
from sqlalchemy import Numeric
from sqlalchemy import String

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from .base import Base
from .base import UUIDMixin
from .base import TimestampMixin


class PurchaseOrderItem(UUIDMixin, TimestampMixin, Base):

    __tablename__ = "purchase_order_items"

    line_no = mapped_column()

    material_code: Mapped[str] = mapped_column(
        String(100),
        nullable=True
    )

    description: Mapped[str] = mapped_column(
        String(500)
    )

    qty = mapped_column(
        Numeric(18,3)
    )

    uom: Mapped[str] = mapped_column(
        String(30)
    )

    weight = mapped_column(
        Numeric(18,3),
        nullable=True
    )

    unit_price = mapped_column(
        Numeric(18,2),
        nullable=True
    )

    purchase_order_id = mapped_column(
        ForeignKey("purchase_orders.id")
    )

    purchase_order = relationship(
        "PurchaseOrder",
        back_populates="items"
    )
