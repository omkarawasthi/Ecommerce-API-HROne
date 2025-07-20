from pydantic import BaseModel, Field, GetJsonSchemaHandler
from pydantic.json_schema import JsonSchemaValue
from typing import List
from bson import ObjectId


class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid ObjectId")
        return ObjectId(v)

    @classmethod
    def __get_pydantic_json_schema__(cls, core_schema, handler: GetJsonSchemaHandler) -> JsonSchemaValue:
        schema = handler(core_schema)
        schema.update(type="string")
        return schema


class Size(BaseModel):
    size: str
    quantity: int


class ProductCreate(BaseModel):
    name: str
    price: float
    sizes: List[Size]


class Product(ProductCreate):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")

    class Config:
        populate_by_name = True  # Updated for Pydantic v2
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}


class OrderItem(BaseModel):
    productId: str
    qty: int


class OrderCreate(BaseModel):
    userId: str
    items: List[OrderItem]


class Order(OrderCreate):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")

    class Config:
        populate_by_name = True  # Updated for Pydantic v2
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
