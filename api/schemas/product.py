from pydantic import BaseModel


class ProductBase(BaseModel):
    name: str
    price: float
    stock: int


class Product(ProductBase):
    id: int

    class Config:
        orm_mode = True
