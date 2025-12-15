from sqlmodel import Session, select
from app.models.order import OrderModel
from app.models.order_item import OrderItemModel
from uuid import UUID
from typing import List


class OrderRepository:
    def __init__(self, db: Session) -> None:
        self.db = db

    def create(self, order: OrderModel) -> OrderModel:
        self.db.add(order)
        self.db.commit()
        self.db.refresh(order)
        return order

    def get_user_orders(self, user_id: int) -> List[OrderModel]:
        return self.db.exec(select(OrderModel).where(OrderModel.user_id == user_id).order_by(OrderModel.created_at.desc())).all()

    def get_order_by_id(self, order_id: UUID) -> OrderModel | None:
        return self.db.exec(select(OrderModel).where(OrderModel.id == order_id)).first()

    def get_order_items(self, order_id: UUID) -> List[OrderItemModel]:
        return self.db.exec(select(OrderItemModel).where(OrderItemModel.order_id == order_id)).all()

    def add_items(self, items: List[OrderItemModel]) -> None:
        self.db.add_all(items)
        self.db.commit()

    def save(self, order: OrderModel) -> None:
        self.db.add(order)
        self.db.commit()
        self.db.refresh(order)
