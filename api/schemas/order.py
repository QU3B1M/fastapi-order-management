from datetime import datetime
from pydantic import BaseModel
from typing import List, Optional


# Shared properties
class OrderBase(BaseModel):
    description: Optional[str]
    customer_id: int
    product_id: int


# Properties to receive on Order creation
class OrderCreate(OrderBase):
    pass
    # products: List[int]


# Properties to receive on Order update
class OrderUpdate(OrderBase):
    # products: List[int]
    pass


# Properties shared by models stored in DB
class OrderInDBBase(OrderBase):
    id: int
    date: Optional[datetime] = datetime.now()

    class Config:
        orm_mode = True


# Properties to return to client
class Order(OrderInDBBase):
    pass


# Properties stored in DB
class OrderInDB(OrderInDBBase):
    pass
