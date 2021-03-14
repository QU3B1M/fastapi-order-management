from typing import List, Any

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api.dependencies.database import get_db
from app.db import models, repositories
from app import schemas


router = APIRouter(prefix="/product", tags=["Product"])


@router.get("/", response_model=List[schemas.Product])
async def product_get_all(db: Session = Depends(get_db)) -> Any:
    """
    Retrieve products.
    """
    products = await repositories.product.get_multi(db=db)
    return products


@router.post("/", response_model=schemas.Product)
async def product_create(
    product_in: schemas.ProductCreate, db: Session = Depends(get_db)
) -> Any:
    """
    Create new product.
    """
    product = await repositories.product.create(db=db, obj_in=product_in)
    return product


@router.get("/{id}")
async def product_get(id: int, db: Session = Depends(get_db)) -> Any:
    """
    Get product by ID.
    """
    product = await repositories.product.get(db=db, id=id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


@router.put("/{id}", response_model=schemas.Product)
async def product_update(
    id: int, product_in: schemas.ProductUpdate, db: Session = Depends(get_db)
) -> Any:
    """
    Update a product.
    """
    product = await repositories.product.get(db=db, id=id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    product = await repositories.product.update(
        db=db, db_obj=product, obj_in=product_in
    )
    return product


@router.delete("/{id}", response_model=schemas.Product)
async def product_delete(id: int, db: Session = Depends(get_db)) -> Any:
    """
    Delete an product.
    """
    product = await repositories.product.get(db=db, id=id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    product = await repositories.product.remove(db=db, id=id)
