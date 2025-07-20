from fastapi import APIRouter, Query, HTTPException
from typing import Optional
from models.models import ProductCreate
from controllers.products import create_product, list_products_controllers

router = APIRouter()

@router.post("", status_code=201)
async def create_product(product: ProductCreate):
    return await create_product(product)

@router.get("")
async def list_products(
    name: Optional[str] = Query(None),
    size: Optional[str] = Query(None),
    limit: Optional[int] = Query(10, ge=1, le=100),
    offset: Optional[int] = Query(0, ge=0)
):
    return await list_products_controllers(name, size, limit, offset)
