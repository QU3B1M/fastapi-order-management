from typing import Optional, List

from pydantic import BaseModel

from api.schemas.order import Order


class ProductBase(BaseModel):
    """
    Schema of the shared properties between every schema.
    """

    name: str
    description: Optional[str]
    price: float
    stock: int


class ProductCreate(ProductBase):
    """
    Schema of the properties to receive on Order creation.
    """

    pass


class ProductUpdate(ProductBase):
    """
    Schema of the properties to receive on Order update.
    """

    pass


class ProductInDBBase(ProductBase):
    """
    Schema of the properties shared by models stored in DB.
    """

    id: int

    class Config:
        orm_mode = True


class Product(ProductInDBBase):
    """
    Schema of the properties to return to client.
    """

    pass


class ProductInDB(ProductInDBBase):
    """
    Schema of the properties stored in DB.
    """

    pass