from pydantic import BaseModel
from typing import List
from datetime import datetime


class OrderBase(BaseModel):
    date: datetime
    customer: CustomerBase
    products: List[ProductBase]
