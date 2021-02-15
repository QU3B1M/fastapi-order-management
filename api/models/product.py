from sqlalchemy import Integer, String, Column, Float
from api.db.base_class import Base


class Product(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    price = Column(Float)
    stock = Column(Integer)
