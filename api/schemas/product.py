from typing import Optional
from pydantic import BaseModel


# Shared properties
class ProductBase(BaseModel):
    name: str
    description: Optional[str]
    price: float
    stock: int


# Properties to receive on Product creation
class ProductCreate(ProductBase):
    pass


# Properties to receive on Product update
class ProductUpdate(ProductBase):
    pass


# Properties shared by models stored in DB
class ProductInDBBase(ProductBase):
    id: int

    class Config:
        orm_mode = True


# Properties to return to client
class Product(ProductInDBBase):
    pass


# Properties properties stored in DB
class ProductInDB(ProductInDBBase):
    pass