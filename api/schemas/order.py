from datetime import datetime
from pydantic import BaseModel
from typing import List, Optional
from api.schemas.product import Product


# Shared properties
class OrderBase(BaseModel):
    date: datetime
    description: Optional[str]
    products: List[Product]


# Properties to receive on Order creation
class OrderCreate(OrderBase):
    pass


# Properties to receive on Order update
class OrderUpdate(OrderBase):
    pass


# Properties shared by models stored in DB
class OrderInDBBase(OrderBase):
    id: int
    customer_id: int

    class Config:
        orm_mode = True


# Properties to return to client
class Order(OrderInDBBase):
    pass


# Properties properties stored in DB
class OrderInDB(OrderInDBBase):
    pass
