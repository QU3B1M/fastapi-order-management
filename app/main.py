from fastapi import FastAPI
from app.db.base import Base
from app.db.session import engine
from app.api import router


Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router)
