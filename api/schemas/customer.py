from typing import List, Optional

from pydantic import BaseModel, EmailStr

from api.schemas.order import Order


class CustomerBase(BaseModel):
    """
    Schema of the shared properties between every schema.
    """

    name: str
    email: EmailStr
    phone_number: int


class CustomerCreate(CustomerBase):
    """
    Schema of the properties to receive on Customer creation.
    """

    pass


class CustomerUpdate(CustomerBase):
    """
    Schema of the properties to receive on Customer update.
    """

    pass


class CustomerInDBBase(CustomerBase):
    """
    Schema of the properties shared by models stored in DB.
    """

    id: int

    class Config:
        orm_mode = True


class Customer(CustomerInDBBase):
    """
    Schema of the properties to return to client.
    """

    pass


class CustomerInDB(CustomerInDBBase):
    """
    Schema of the properties stored in DB.
    """

    pass
