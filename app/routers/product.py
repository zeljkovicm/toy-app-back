from fastapi import APIRouter, Depends
from sqlmodel import Session
from app.core.db import get_db
from app.services.product_service import ProductService
from app.schemas.product import Product
from typing import List

router = APIRouter()


@router.get("/", response_model=List[Product])
async def get_products(db: Session = Depends(get_db)):
    return await ProductService.get_all_products(db)


@router.get("/permalink/{permalink}", response_model=Product)
async def get_product(permalink: str, db: Session = Depends(get_db)):
    return await ProductService.get_product_by_permalink(db, permalink)
