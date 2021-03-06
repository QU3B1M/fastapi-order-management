from api.repositories.base import BaseRepository
from api.models.product import Product
from api.schemas.product import ProductCreate, ProductUpdate


class ProductRepository(BaseRepository[Product, ProductCreate, ProductUpdate]):
    """
    Class with methods to Create, Read, Update and Delete a Product.
    """

    pass


product = ProductRepository(Product)