from typing import List

from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder

from app.db.repositories.base import BaseRepository
from app.db.models.order import Order
from app.schemas.order import OrderCreate, OrderUpdate


class OrderRepository(BaseRepository[Order, OrderCreate, OrderUpdate]):
    """
    Class with methods to Create, Read, Update and Delete an Order.
    """

    async def get_multi_by_customer(
        self, db: Session, *, customer_id: int, skip: int = 0, limit: int = 100
    ) -> List[Order]:
        """
        Method to Read multiple Orders by the Customer ID.
        """
        return (
            db.query(self.model)
            .filter(self.model.customer_id == customer_id)
            .offset(skip)
            .limit(limit)
            .all()
        )


order = OrderRepository(Order)
