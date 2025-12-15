from sqlmodel import Session
from uuid import UUID

from app.repositories.order_repository import OrderRepository
from app.schemas.order import OrderRequest, OrderUpdateRequest
from app.models.order import OrderModel
from app.models.order_item import OrderItemModel
from app.exceptions.exceptions import OrderNotFound


class OrderService:
    def __init__(self, db: Session) -> None:
        self.repository = OrderRepository(db)

    def create_order(self, data: OrderRequest, user_id: UUID):
        total = 0
        for item in data.items:
            total += item.quantity * item.price

        payment_status = ""
        if data.payment_type == "cash":
            payment_status = "pending"
        else:
            payment_status = "success"

        order = OrderModel(
            user_id=user_id,
            total=total,
            payment_type=data.payment_type,
            payment_status=payment_status,
            order_status="created",
            delivery_status="pending",
            phone=data.phone,
            address=data.address,
            city=data.city,
            zip=data.zip
        )

        order = self.repository.create(order)

        items = []

        for item in data.items:
            order_item = OrderItemModel(
                order_id=order.id,
                toy_id=item.toy_id,
                quantity=item.quantity,
                price=item.price
            )
            items.append(order_item)

        self.repository.add_items(items)
        return order

    def update_order_status(self, order_id: UUID, data: OrderUpdateRequest):
        order = self.repository.get_order_by_id(order_id)
        if not order:
            raise OrderNotFound(f"Narudžbina #{order_id} ne postoji")

        if data.cancel is True:
            order.delivery_status = 'canceled'
            order.payment_status = 'canceled'
            order.order_status = 'canceled'

        if data.order_status is not None:
            order.order_status = data.order_status

        if data.payment_status is not None:
            order.payment_status = data.payment_status

        if data.delivery_status is not None:
            order.delivery_status = data.delivery_status

        self.repository.save(order)
        return order

    def get_my_orders(self, user_id: UUID) -> list[OrderModel]:
        return self.repository.get_user_orders(user_id)
