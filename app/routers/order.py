from fastapi import APIRouter, Depends, status
from sqlmodel import Session
from uuid import UUID
from typing import List

from app.core.db import get_db
from app.core.dependencies import get_current_user
from app.schemas.order import OrderRequest, OrderResponse, OrderUpdateRequest
from app.services.order_service import OrderService
from app.core.dependencies import get_order_service

router = APIRouter()


@router.post("/create", response_model=OrderResponse, status_code=status.HTTP_201_CREATED)
def create_order(payload: OrderRequest, order_service: OrderService = Depends(get_order_service), user=Depends(get_current_user)):
    return order_service.create_order(payload, user.id)


@router.patch("/{order_id}", response_model=OrderResponse)
def update_order_status(order_id: UUID, payload: OrderUpdateRequest, order_service: OrderService = Depends(get_order_service)):
    return order_service.update_order_status(order_id, payload)


@router.get("/my_orders", response_model=List[OrderResponse])
def get_my_orders(order_service: OrderService = Depends(get_order_service), user=Depends(get_current_user)):
    return order_service.get_my_orders(user.id)
