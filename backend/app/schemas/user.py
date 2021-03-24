from typing import Optional, List

from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    """
    Schema of the shared properties between every schema.
    """

    username: str
    full_name: Optional[str]
    email: EmailStr
    is_superuser: bool = False


class UserCreate(UserBase):
    """
    Schema of the properties to receive on Order creation.
    """

    password: str


class UserUpdate(UserBase):
    """
    Schema of the properties to receive on Order update.
    """

    password: Optional[str]


class UserInDBBase(UserBase):
    """
    Schema of the properties shared by models stored in DB.
    """

    id: int
    hashed_password: str

    class Config:
        orm_mode = True


class User(UserInDBBase):
    """
    Schema of the properties to return to client.
    """

    pass


class UserInDB(UserInDBBase):
    """
    Schema of the properties stored in DB.
    """

    pass
