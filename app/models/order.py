from sqlmodel import SQLModel, Field, Relationship
from uuid import UUID, uuid4
from datetime import datetime
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.order_item import OrderItemModel


class OrderModel(SQLModel, table=True):
    __tablename__ = "order"

    id: UUID = Field(default_factory=uuid4, primary_key=True, index=True)
    user_id: UUID = Field(index=True, nullable=False)
    total: float
    payment_type: str
    payment_status: str
    order_status: str
    delivery_status: str
    phone: str
    address: str
    city: str
    zip: str
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    created_at: datetime = Field(default_factory=datetime.utcnow)

    items: List["OrderItemModel"] = Relationship(back_populates="order")
