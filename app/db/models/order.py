from sqlalchemy import Integer, Column, DateTime, ForeignKey, String, Table, ARRAY
from sqlalchemy.orm import relationship
from app.db.base_class import Base


class Order(Base):
    id = Column(Integer, primary_key=True, index=True)
    date = Column(DateTime)
    description = Column(String)
    customer_id = Column(Integer, ForeignKey("customer.id"))
    product_id = Column(Integer, ForeignKey("product.id"))
    product = relationship("Product", back_populates="orders")
    customer = relationship("Customer", back_populates="orders")
