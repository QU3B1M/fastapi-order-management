from typing import List, Optional
from pydantic import BaseModel
from api.schemas.order import Order


# Shared properties
class CustomerBase(BaseModel):
    name: str
    email: str
    phone_number: int


# Properties to receive on Customer creation
class CustomerCreate(CustomerBase):
    pass


# Properties to receive on Customer update
class CustomerUpdate(CustomerBase):
    pass


# Properties shared by models stored in DB
class CustomerInDBBase(CustomerBase):
    id: int
    orders: Optional[List[Order]]

    class Config:
        orm_mode = True


# Properties to return to client
class Customer(CustomerInDBBase):
    pass


# Properties properties stored in DB
class CustomerInDB(CustomerInDBBase):
    pass
