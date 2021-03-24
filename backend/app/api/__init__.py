from fastapi import APIRouter

from app.api.routers import customer, product, order, user, auth


router = APIRouter()

router.include_router(user.router)
router.include_router(order.router)
router.include_router(product.router)
router.include_router(customer.router)
router.include_router(auth.router)
