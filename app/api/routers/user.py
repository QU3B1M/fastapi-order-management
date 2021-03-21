from typing import List, Any

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api.dependencies.database import get_db
from app.api.dependencies.authentication import get_current_user
from app.db import models, repositories
from app import schemas


router = APIRouter(prefix="/user", tags=["user"])


@router.get("/", response_model=List[schemas.User])
async def user_get_all(
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(get_current_user),
) -> Any:
    """
    Retrieve users.
    """
    users = await repositories.user.get_multi(db=db)
    return users


@router.get("/me", response_model=schemas.User)
async def read_users_me(current_user: schemas.User = Depends(get_current_user)):

    return current_user


@router.post("/", response_model=schemas.User)
async def user_create(
    user_in: schemas.UserCreate, db: Session = Depends(get_db)
) -> Any:
    """
    Create new user.
    """
    user = await repositories.user.create(db=db, obj_in=user_in)
    return user


@router.get("/{id}")
async def user_get(
    id: int,
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(get_current_user),
) -> Any:
    """
    Get user by ID.
    """
    user = await repositories.user.get(db=db, id=id)
    if not user:
        raise HTTPException(status_code=404, detail="user not found")
    return user


@router.put("/{id}", response_model=schemas.User)
async def user_update(
    id: int,
    user_in: schemas.UserUpdate,
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(get_current_user),
) -> Any:
    """
    Update a user.
    """
    user = await repositories.user.get(db=db, id=id)
    if not user:
        raise HTTPException(status_code=404, detail="user not found")
    user = await repositories.user.update(db=db, db_obj=user, obj_in=user_in)
    return user


@router.delete("/{id}", response_model=schemas.User)
async def user_delete(
    id: int,
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(get_current_user),
) -> Any:
    """
    Delete an user.
    """
    user = await repositories.user.get(db=db, id=id)
    if not user:
        raise HTTPException(status_code=404, detail="user not found")
    user = await repositories.user.remove(db=db, id=id)
