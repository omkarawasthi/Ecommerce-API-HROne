from models import OrderCreate
from fastapi import HTTPException
from database import get_database
from bson import ObjectId
from datetime import datetime

db = get_database()

async def create_order(order: OrderCreate):
    try:
        product_ids = [item.productId for item in order.items]
        existing = list(db.products.find({"_id": {"$in": [ObjectId(pid) for pid in product_ids]}}))

        if len(existing) != len(product_ids):
            raise HTTPException(status_code=400, detail="One or more products not found")

        order_dict = order.dict()
        order_dict["created_at"] = datetime.utcnow()

        result = db.orders.insert_one(order_dict)
        return {"id": str(result.inserted_id)}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

async def get_user_orders_controller(user_id, limit, offset):
    try:
        query_filter = {"userId": user_id}
        total_count = db.orders.count_documents(query_filter)
        cursor = db.orders.find(query_filter).sort("_id", 1).skip(offset).limit(limit)

        orders = []
        for order in cursor:
            items_with_details = []
            for item in order["items"]:
                product = db.products.find_one({"_id": ObjectId(item["productId"])})
                if product:
                    items_with_details.append({
                        "productDetails": {
                            "name": product["name"],
                            "id": item["productId"]
                        },
                        "qty": item["qty"]
                    })
            orders.append({
                "id": str(order["_id"]),
                "items": items_with_details
            })

        next_offset = offset + limit if offset + limit < total_count else None
        prev_offset = max(0, offset - limit) if offset > 0 else None

        return {
            "data": orders,
            "total": float(total_count),
            "page": {
                "next": str(next_offset) if next_offset is not None else None,
                "limit": limit,
                "previous": str(prev_offset) if prev_offset is not None else None
            }
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
