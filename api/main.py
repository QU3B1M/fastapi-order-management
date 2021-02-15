from fastapi import FastAPI
from api.db.base import Base
from api.db.session import engine

Base.metadata.create_all(bind=engine)

app = FastAPI()
