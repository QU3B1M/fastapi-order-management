from datetime import timedelta

from fastapi.security import OAuth2PasswordRequestForm
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.security import create_access_token
from app.core.config import settings
from app.api.dependencies.database import get_db
from app.api.utils import incorrect_password
from app.db import repositories
from app import schemas


router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post("/login", response_model=schemas.Token)
async def login(
    db: Session = Depends(get_db), form_data: OAuth2PasswordRequestForm = Depends()
) -> schemas.Token:
    user = await repositories.user.authenticate(
        db=db, username=form_data.username, password=form_data.password
    )
    if not user:
        raise incorrect_password
    expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(subject=user.username, expires_delta=expires)

    return {"access_token": access_token, "token_type": "bearer"}
