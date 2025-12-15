from sqlmodel import SQLModel, Field, Relationship
from uuid import UUID, uuid4
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.order import OrderModel


class OrderItemModel(SQLModel, table=True):
    __tablename__ = "order_item"

    id: UUID = Field(default_factory=uuid4, primary_key=True)
    order_id: UUID = Field(foreign_key="order.id", index=True)
    toy_id: int
    quantity: int
    price: float

    order: Optional["OrderModel"] = Relationship(back_populates="items")
