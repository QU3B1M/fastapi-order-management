from pydantic import BaseModel
from typing import List
from api.schemas.order import Order


class CustomerBase(BaseModel):
    name: str
    email: str
    phone_number: int


class Customer(CustomerBase):
    id: int
    orders: List[Order] = []

    class Config:
        orm_mode = True
