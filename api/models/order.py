from sqlalchemy import Integer, Column, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from api.db.base import Base


class Order(Base):
    id = Column(Integer, primary_key=True, index=True)
    date = Column(DateTime)
    customer_id = Column(Integer, ForeignKey("customer.id"))
    products = relationship("Products")
    customer = relationship("Customer", back_populates="orders")
