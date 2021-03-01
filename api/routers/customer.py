from typing import List, Any

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from api.core.dependencies import get_db
from api import crud, models, schemas


router = APIRouter(prefix="/customer", tags=["Customer"])


@router.get("/", response_model=List[schemas.Customer])
async def customer_get_all(db: Session = Depends(get_db)) -> Any:
    """
    Retrieve customers.
    """
    customers = crud.customer.get_multi(db=db)
    return customers


@router.post("/", response_model=schemas.Customer)
async def customer_create(
    customer_in: schemas.CustomerCreate, db: Session = Depends(get_db)
) -> Any:
    """
    Create new customer.
    """
    customer = crud.customer.create(db=db, obj_in=customer_in)
    return customer


@router.get("/{id}")
async def customer_get(id: int, db: Session = Depends(get_db)) -> Any:
    """
    Get customer by ID.
    """
    customer = crud.customer.get(db=db, id=id)
    if not customer:
        raise HTTPException(status_code=404, detail="customer not found")
    return customer


@router.put("/{id}", response_model=schemas.Customer)
async def customer_update(
    id: int, customer_in: schemas.CustomerUpdate, db: Session = Depends(get_db)
) -> Any:
    """
    Update a customer.
    """
    customer = crud.customer.get(db=db, id=id)
    if not customer:
        raise HTTPException(status_code=404, detail="customer not found")
    customer = crud.customer.update(db=db, db_obj=customer, obj_in=customer_in)
    return customer


@router.delete("/{id}", response_model=schemas.Customer)
async def customer_delete(id: int, db: Session = Depends(get_db)) -> Any:
    """
    Delete an customer.
    """
    customer = crud.customer.get(db=db, id=id)
    if not customer:
        raise HTTPException(status_code=404, detail="customer not found")
    customer = crud.customer.remove(db=db, id=id)
