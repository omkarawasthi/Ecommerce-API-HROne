from models import ProductCreate
from fastapi import HTTPException
from database import get_database
from bson import ObjectId

db = get_database()

async def create_product(product: ProductCreate):
    try:
        product_dict = product.dict()
        result = db.products.insert_one(product_dict)
        return {"id": str(result.inserted_id)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

async def list_products_controllers(name, size, limit, offset):
    try:
        query_filter = {}

        if name:
            query_filter["name"] = {"$regex": name, "$options": "i"}
        if size:
            query_filter["sizes.size"] = size

        total_count = db.products.count_documents(query_filter)
        cursor = db.products.find(query_filter).sort("_id", 1).skip(offset).limit(limit)

        products = [
            {
                "id": str(p["_id"]),
                "name": p["name"],
                "price": p["price"]
            }
            for p in cursor
        ]

        next_offset = offset + limit if offset + limit < total_count else None
        prev_offset = max(0, offset - limit) if offset > 0 else None

        return {
            "data": products,
            "page": {
                "next": str(next_offset) if next_offset is not None else None,
                "limit": limit,
                "previous": str(prev_offset) if prev_offset is not None else None
            }
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
