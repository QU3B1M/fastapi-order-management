from typing import Any, Dict, Optional, Union

from sqlalchemy.orm import Session

from app.db.repositories.base import BaseRepository
from app.db.models.user import User
from app.schemas.user import UserCreate, UserUpdate
from app.core.security import get_password_hash, verify_password


class UserRepository(BaseRepository[User, UserCreate, UserUpdate]):
    """
    Class with methods to Create, Read, Update and Delete a User.
    """

    async def create(self, db: Session, *, obj_in: UserCreate) -> User:
        """Method to Create a user with its password hashed."""
        db_obj = User(
            username=obj_in.username,
            email=obj_in.email,
            hashed_password=get_password_hash(obj_in.password),
            full_name=obj_in.full_name,
            is_superuser=obj_in.is_superuser,
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    async def get_by_email(self, db: Session, *, email: str) -> Optional[User]:
        """Method to Read a User from Database by its email."""

        return db.query(User).filter(User.email == email).first()

    async def get_by_username(self, db: Session, *, username: str) -> Optional[User]:
        """Method to Read a User from Database by its username."""

        return db.query(User).filter(User.username == username).first()

    async def authenticate(
        self, db: Session, *, username: str, password: str
    ) -> Optional[User]:
        """Method to authenticate the user by verifying its password."""
        user = await self.get_by_username(db, username=username)
        if not user:
            return None
        if not verify_password(password, user.hashed_password):
            return None
        return user

    async def is_superuser(self, user: User) -> bool:
        """Method to check if the user is superuser or admin."""

        return user.is_superuser


user = UserRepository(User)
