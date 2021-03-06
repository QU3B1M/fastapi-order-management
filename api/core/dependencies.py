from typing import Generator

from api.db.session import SessionLocal


async def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
