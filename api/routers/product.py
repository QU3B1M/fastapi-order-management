from fastapi import APIRouter, status


router = APIRouter(prefix="/product", tags=["Product"])


@router.post("/")
async def product_create():
    return status.HTTP_200_OK


@router.get("/all")
async def product_get_all():
    return {"products": ["fake_product_1", "fake_product_2"]}


@router.get("/{id}")
async def product_get(id: int):
    return {"product": "a_fake_product"}
