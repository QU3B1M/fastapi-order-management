from fastapi import FastAPI
from api.db.base import Base
from api.db.session import engine
from api.routers import customer, product, order


Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(customer.router)
app.include_router(product.router)
app.include_router(order.router)
