from sqlalchemy import Integer, String, Column, Float
from sqlalchemy.orm import relationship
from app.db.base_class import Base


class Product(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    description = Column(String)
    price = Column(Float)
    stock = Column(Integer)
    orders = relationship("Order", back_populates="product")
