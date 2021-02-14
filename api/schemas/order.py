from datetime import datetime
from pydantic import BaseModel
from typing import List
from api.schemas.product import Product


class OrderBase(BaseModel):
    date: datetime
    products: List[Product]


class Order(OrderBase):
    id: int
    customer_id: int

    class Config:
        orm_mode = True
