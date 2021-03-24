from app.db.repositories.base import BaseRepository
from app.db.models.product import Product
from app.schemas.product import ProductCreate, ProductUpdate


class ProductRepository(BaseRepository[Product, ProductCreate, ProductUpdate]):
    """
    Class with methods to Create, Read, Update and Delete a Product.
    """

    pass


product = ProductRepository(Product)