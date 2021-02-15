from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from api.core.config import settings


engine = create_engine(
    settings.SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    pool_pre_ping=True,
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
