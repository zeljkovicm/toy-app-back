import httpx
from typing import List
from app.schemas.product import Product, AgeGroup, ProductType


class PequlaService:
    BASE_URL = "https://toy.pequla.com/api"

    @staticmethod
    async def get_all_toys() -> List[Product]:
        url = f"{PequlaService.BASE_URL}/toy"
        async with httpx.AsyncClient() as client:
            resp = await client.get(url)
        resp.raise_for_status()
        data = resp.json()
        return [Product(**item) for item in data]

    @staticmethod
    async def get_toy_by_id(toy_id: int) -> Product:
        url = f"{PequlaService.BASE_URL}/toy/{toy_id}"
        async with httpx.AsyncClient() as client:
            resp = await client.get(url)
        resp.raise_for_status()
        return Product(**resp.json())

    @staticmethod
    async def get_toy_by_permalink(permalink: str) -> Product:
        url = f"{PequlaService.BASE_URL}/toy/permalink/{permalink}"
        async with httpx.AsyncClient() as client:
            resp = await client.get(url)
        resp.raise_for_status()
        return Product(**resp.json())

    @staticmethod
    async def get_toys_by_ids(ids: List[int]) -> List[Product]:
        url = f"{PequlaService.BASE_URL}/toy/list"
        async with httpx.AsyncClient() as client:
            resp = await client.post(url, json=ids)
        resp.raise_for_status()
        data = resp.json()
        return [Product(**item) for item in data]

    @staticmethod
    async def get_age_groups() -> List[AgeGroup]:
        url = f"{PequlaService.BASE_URL}/age-group"
        async with httpx.AsyncClient() as client:
            resp = await client.get(url)
        resp.raise_for_status()
        data = resp.json()
        return [AgeGroup(**item) for item in data]

    @staticmethod
    async def get_types() -> List[ProductType]:
        url = f"{PequlaService.BASE_URL}/type"
        async with httpx.AsyncClient() as client:
            resp = await client.get(url)
        resp.raise_for_status()
        data = resp.json()
        return [ProductType(**item) for item in data]
