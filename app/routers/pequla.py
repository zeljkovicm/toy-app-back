from fastapi import APIRouter
from typing import List
from app.services.pequla_service import PequlaService
from app.schemas.product import Product, AgeGroup, ProductType

router = APIRouter()


@router.get("/", response_model=List[Product])
async def get_all_products():
    return await PequlaService.get_all_toys()


@router.get("/{toy_id}", response_model=Product)
async def get_product_by_id(toy_id: int):
    return await PequlaService.get_toy_by_id(toy_id)


@router.get("/permalink/{permalink}", response_model=Product)
async def get_product_by_permalink(permalink: str):
    return await PequlaService.get_toy_by_permalink(permalink)


@router.get("/age-groups", response_model=List[AgeGroup])
async def get_age_groups():
    return await PequlaService.get_age_groups()


@router.get("/types", response_model=List[ProductType])
async def get_types():
    return await PequlaService.get_types()
