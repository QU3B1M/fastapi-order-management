from typing import List, Any

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api.dependencies.database import get_db
from app.api.dependencies.authentication import get_current_user
from app.db import models, repositories
from app import schemas


router = APIRouter(prefix="/order", tags=["Order"])


@router.get("/", response_model=List[schemas.Order])
async def order_get_all(
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(get_current_user),
) -> Any:
    """
    Retrieve orders.
    """
    orders = await repositories.order.get_multi(db=db)
    return orders


@router.get("/customer/{id}", response_model=List[schemas.Order])
async def order_get_all_by_customer(
    id: int,
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(get_current_user),
) -> Any:
    """
    Retrieve orders.
    """
    orders = await repositories.order.get_multi_by_customer(db=db, customer_id=id)
    return orders


@router.post("/", response_model=schemas.Order)
async def order_create(
    order_in: schemas.OrderCreate,
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(get_current_user),
) -> Any:
    """
    Create new order.
    """
    order = await repositories.order.create(db=db, obj_in=order_in)
    return order


@router.get("/{id}")
async def order_get(
    id: int,
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(get_current_user),
) -> Any:
    """
    Get order by ID.
    """
    order = await repositories.order.get(db=db, id=id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order


@router.put("/{id}", response_model=schemas.Order)
async def order_update(
    id: int,
    order_in: schemas.OrderUpdate,
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(get_current_user),
) -> Any:
    """
    Update a order.
    """
    order = await repositories.order.get(db=db, id=id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    order = await repositories.order.update(db=db, db_obj=order, obj_in=order_in)
    return order


@router.delete("/{id}", response_model=schemas.Order)
async def order_delete(
    id: int,
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(get_current_user),
) -> Any:
    """
    Delete an order.
    """
    order = await repositories.order.get(db=db, id=id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    order = await repositories.order.remove(db=db, id=id)
