from fastapi import APIRouter, Query, HTTPException
from typing import Optional
from models.models import OrderCreate
from controllers.orders import create_order, get_user_orders

router = APIRouter()

@router.post("", status_code=201)
async def create_order(order: OrderCreate):
    return await create_order(order)

@router.get("/{user_id}")
async def get_user_orders(
    user_id: str,
    limit: Optional[int] = Query(10, ge=1, le=100),
    offset: Optional[int] = Query(0, ge=0)
):
    return await get_user_orders(user_id, limit, offset)
