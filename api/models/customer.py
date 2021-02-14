from sqlalchemy import Integer, String, Column
from sqlalchemy.orm import relationship
from api.db.base import Base


class Customer(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True, index=True)
    phone_number = Column(Integer)
    orders = relationship("Order", back_populates="customer")
