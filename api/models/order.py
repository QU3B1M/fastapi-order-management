from sqlalchemy import Integer, Column, DateTime, ForeignKey, String, Table, ARRAY
from sqlalchemy.orm import relationship
from api.db.base_class import Base


products_in_orders = Table(
    "products_in_orders",
    Base.metadata,
    Column("order_id", Integer, ForeignKey("order.id")),
    Column("product_id", Integer, ForeignKey("product.id")),
)


class Order(Base):
    id = Column(Integer, primary_key=True, index=True)
    date = Column(DateTime)
    description = Column(String)
    customer_id = Column(Integer, ForeignKey("customer.id"))
    products_ids = relationship("Product", secondary=products_in_orders)
    customer = relationship("Customer", back_populates="orders")
