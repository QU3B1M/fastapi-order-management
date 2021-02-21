from fastapi import APIRouter, status


router = APIRouter(prefix="/order", tags=["Order"])


@router.post("/")
async def order_create():
    return status.HTTP_200_OK


@router.get("/all")
async def order_get_all():
    return {"orders": ["fake_order_1", "fake_order_2"]}


@router.get("/{id}")
async def order_get(id: int):
    return {"order": "a_fake_order"}
