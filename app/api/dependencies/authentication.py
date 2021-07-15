from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends
from jose import JWTError, jwt

from app.core.config import settings
from app.api.dependencies.database import get_db
from app.api.utils import credentials_exception
from app.schemas.token import TokenData
from app.db import repositories


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


async def get_current_user(
    token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)
):
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[settings.SIGNING_ALGORITHM]
        )
        sub: str = payload.get("sub")
        if sub is None:
            raise credentials_exception
        token_data = TokenData(sub=sub)
    except JWTError:
        raise credentials_exception
    user = repositories.user.get_by_username(db=db, username=token_data.sub)
    if user is None:
        raise credentials_exception
    return user
