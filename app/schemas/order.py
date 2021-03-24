from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, validator


class OrderBase(BaseModel):
    """
    Schema of the shared properties between every schema.
    """

    description: Optional[str]
    customer_id: int
    product_id: int


class OrderCreate(OrderBase):
    """
    Schema of the properties to receive on Customer creation.
    """

    pass


class OrderUpdate(OrderBase):
    """
    Schema of the properties to receive on Customer update.
    """

    pass


class OrderInDBBase(OrderBase):
    """
    Schema of the properties shared by models stored in DB.
    """

    id: int
    date: Optional[datetime]

    @validator("date")
    def date_validator(cls, v):
        if not v:
            return datetime.now()
        return v

    class Config:
        orm_mode = True


class Order(OrderInDBBase):
    """
    Schema of the properties to return to client.
    """

    pass


class OrderInDB(OrderInDBBase):
    """
    Schema of the properties stored in DB.
    """

    pass
