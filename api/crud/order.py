from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder

from api.crud.base import CRUDBase
from api.models.order import Order
from api.schemas.order import OrderCreate, OrderUpdate


class CRUDOrder(CRUDBase[Order, OrderCreate, OrderUpdate]):
    pass


order = CRUDOrder(Order)
