from app.schemas.camel_case_model import CamelCaseModel
from typing import List
from uuid import UUID
from datetime import datetime


class OrderItem(CamelCaseModel):
    toy_id: int
    quantity: int
    price: float


class OrderRequest(CamelCaseModel):
    phone: str
    address: str
    city: str
    zip: str
    payment_type: str
    items: List[OrderItem]


class OrderResponse(CamelCaseModel):
    id: UUID
    total: float
    payment_type: str
    payment_status: str
    order_status: str
    delivery_status: str
    phone: str
    address: str
    city: str
    zip: str
    created_at: datetime
    updated_at: datetime
    items: List[OrderItem]


class OrderUpdateRequest(CamelCaseModel):
    order_status: str | None = None
    payment_status: str | None = None
    delivery_status: str | None = None
    cancel: bool | None = None
