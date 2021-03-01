from api.crud.base import CRUDBase
from api.models.product import Product
from api.schemas.product import ProductCreate, ProductUpdate


class CRUDProduct(CRUDBase[Product, ProductCreate, ProductUpdate]):
    pass


product = CRUDProduct(Product)