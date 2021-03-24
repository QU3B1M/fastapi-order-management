from fastapi import FastAPI
from app.db.base import Base
from app.db.session import engine
from app.routers import customer, product, order


Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(customer.router)
app.include_router(product.router)
app.include_router(order.router)
