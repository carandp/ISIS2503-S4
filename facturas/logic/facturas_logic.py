"""
This module contains the logic for the facturas app.
Main functions:
- get_facturas: Get a list of all facturas
- get_factura: Get a single factura
- create_factura: Create a new factura
- update_factura: Update a factura
- delete_factura: Delete a factura
"""
import os
from bson import ObjectId as BsonObjectId
import requests
from models.models import Factura, FacturaCollection
from models.db import facturas_collection
from pymongo.errors import DuplicateKeyError
from fastapi import HTTPException

PATH_API_GATEWAY = "http://" + os.environ.get("KONG_HOST", "10.128.0.81") + ":" + os.environ.get("KONG_PORT", "8000")
PATH_NOT = PATH_API_GATEWAY + "/notificaciones"

async def get_facturas():
    """
    Get a list of facturas
    :return: A list of facturas
    """
    facturas = await facturas_collection.find().to_list(1000)
    return FacturaCollection(facturas=facturas)

async def get_factura(factura_id: str):
    """
    Get a single factura
    :param factura_id: The id of the factura
    :return: The factura
    """
    if not BsonObjectId.is_valid(factura_id):
        raise HTTPException(status_code=400, detail="Invalid factura ID format")

    if (factura := await facturas_collection.find_one({"_id": BsonObjectId(factura_id)})) is not None:
        return factura

    raise HTTPException(
        status_code=404, detail=f"Factura with id {factura_id} not found"
    )

async def create_factura(factura: Factura):
    """
    Insert a new factura record.
    """
    try:
        new_factura = await facturas_collection.insert_one(
            factura.model_dump(by_alias=True, exclude={"id"})
        )
        created_factura = await facturas_collection.find_one({"_id": new_factura.inserted_id})
        if (created_factura["notificar"]):
            data = {
                "id": str(created_factura["_id"]),
                "institucion": created_factura["institucion"],
                "tipo": created_factura["tipo"],
                "descripcion": created_factura["descripcion"],
                "total": created_factura["total"],
                "correo": created_factura["correo"]
            }
            r = requests.post(PATH_NOT, json=data)
            print(r.status_code)
        return created_factura

    except DuplicateKeyError:
        raise HTTPException(
            status_code=409, detail="Factura with the same unique fields already exists"
        )

async def update_factura(factura_id: str, factura: Factura):
    """
    Update a factura
    :param factura_id: The id of the factura
    :param factura: The factura data
    :return: The updated factura
    """
    if not BsonObjectId.is_valid(factura_id):
        raise HTTPException(status_code=400, detail="Invalid factura ID format")

    try:
        update_result = await facturas_collection.update_one(
            {"_id": BsonObjectId(factura_id)},
            {"$set": factura.model_dump(by_alias=True, exclude={"id"})},
        )
        if update_result.modified_count == 1:
            if (
                updated_factura := await facturas_collection.find_one({"_id": BsonObjectId(factura_id)})
            ) is not None:
                return updated_factura
    except DuplicateKeyError:
        raise HTTPException(
            status_code=409, detail="Factura with the same unique fields already exists"
        )

    raise HTTPException(
        status_code=404,
        detail=f"Factura with id {factura_id} not found or no updates were made",
    )

async def delete_factura(factura_id: str):
    """
    Delete a factura
    :param factura_id: The id of the factura
    """
    if not BsonObjectId.is_valid(factura_id):
        raise HTTPException(status_code=400, detail="Invalid factura ID format")

    delete_result = await facturas_collection.delete_one({"_id": BsonObjectId(factura_id)})

    if delete_result.deleted_count == 1:
        return

    raise HTTPException(
        status_code=404, detail=f"Factura with id {factura_id} not found"
    )