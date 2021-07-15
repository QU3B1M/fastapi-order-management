from sqlalchemy import Integer, String, Column, Boolean
from app.db.base_class import Base


class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    full_name = Column(String)
    is_superuser = Column(Boolean(), default=False)
    hashed_password = Column(String)
