from fastapi import APIRouter, status


router = APIRouter(prefix="/customer", tags=["Customer"])


@router.post("/")
async def customer_create():
    return status.HTTP_200_OK


@router.get("/all")
async def customer_get_all():
    return {"customers": ["fake_customer_1", "fake_customer_2"]}


@router.get("/{id}")
async def customer_get(id: int):
    return {"customer": "a_fake_customer"}
