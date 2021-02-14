from pydantic import BaseModel


class CustomerBase(BaseModel):
    name: str
    phone_number: int
