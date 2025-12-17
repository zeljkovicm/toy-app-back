from fastapi import APIRouter, Depends
from sqlmodel import Session
from app.core.db import get_db
from app.core.dependencies import get_product_service
from app.services.product_service import ProductService
from app.schemas.product import Product
from typing import List

router = APIRouter()


@router.get("/")
def get_products(product_service=Depends(get_product_service)):
    return product_service.get_all_products()
