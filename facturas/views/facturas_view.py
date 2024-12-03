from fastapi import APIRouter, status, Body
import logic.facturas_logic as facturas_service
from models.models import Factura, FacturaOut, FacturaCollection

router = APIRouter()
ENDPOINT_NAME = "/facturas"


@router.get(
    "/",
    response_description="List all facturas",
    response_model=FacturaCollection,
    status_code=status.HTTP_200_OK,
)
async def get_facturas():
    return await facturas_service.get_facturas()


@router.get(
    "/{factura_code}",
    response_description="Get a single factura by its code",
    response_model=FacturaOut,
    status_code=status.HTTP_200_OK,
)
async def get_factura(factura_code: str):
    return await facturas_service.get_factura(factura_code)


@router.post(
    "/",
    response_description="Create a new factura",
    response_model=FacturaOut,
    status_code=status.HTTP_201_CREATED,
)
async def create_factura(factura: Factura = Body(...)):
    return await facturas_service.create_factura(factura)


@router.put(
    "/{factura_code}",
    response_description="Update a factura",
    response_model=FacturaOut,
    status_code=status.HTTP_200_OK,
)
async def update_factura(factura_code: str, factura: Factura = Body(...)):
    return await facturas_service.update_factura(factura_code, factura)


@router.delete(
    "/{factura_code}",
    response_description="Delete a factura",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_factura(factura_code: str):
    return await facturas_service.delete_factura(factura_code)
