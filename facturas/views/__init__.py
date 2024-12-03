from fastapi import APIRouter

from views import facturas_view

API_PREFIX = "/api"
router = APIRouter()

router.include_router(facturas_view.router, prefix=facturas_view.ENDPOINT_NAME)