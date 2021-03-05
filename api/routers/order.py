from typing import List, Any

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from api.core.dependencies import get_db
from api import crud, models, schemas


router = APIRouter(prefix="/order", tags=["Order"])


@router.get("/", response_model=List[schemas.Order])
async def order_get_all(db: Session = Depends(get_db)) -> Any:
    """
    Retrieve orders.
    """
    orders = crud.order.get_multi(db=db)
    return orders


@router.post("/", response_model=schemas.Order)
async def order_create(
    order_in: schemas.OrderCreate, db: Session = Depends(get_db)
) -> Any:
    """
    Create new order.
    """
    order = crud.order.create(db=db, obj_in=order_in)
    return order


@router.get("/{id}")
async def order_get(id: int, db: Session = Depends(get_db)) -> Any:
    """
    Get order by ID.
    """
    order = crud.order.get(db=db, id=id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order


@router.put("/{id}", response_model=schemas.Order)
async def order_update(
    id: int, order_in: schemas.OrderUpdate, db: Session = Depends(get_db)
) -> Any:
    """
    Update a order.
    """
    order = crud.order.get(db=db, id=id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    order = crud.order.update(db=db, db_obj=order, obj_in=order_in)
    return order


@router.delete("/{id}", response_model=schemas.Order)
async def order_delete(id: int, db: Session = Depends(get_db)) -> Any:
    """
    Delete an order.
    """
    order = crud.order.get(db=db, id=id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    order = crud.order.remove(db=db, id=id)
