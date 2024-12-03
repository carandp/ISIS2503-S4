# Models for the facturas microservice

import uuid
from enum import Enum
from bson import ObjectId
from pydantic import BaseModel, Field, ConfigDict
from typing import List
from models.db import PyObjectId


class Factura(BaseModel):
    institucion: str = Field(...)
    tipo: str = Field(...)
    descripcion: str = Field(...)
    total: float = Field(...)
    notificar: bool = Field(default=False)
    correo: str = Field(default=None)
    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
        json_schema_extra={
            "example": {
                "institucion": "Colegio",
                "tipo": "Alimentacion",
                "descripcion": "Factura por alimentacion: empanadas [x10]",
                "total": 100.0,
                "notificar": False,
                "correo": "",
            }
        },
    )


class FacturaOut(Factura):
    id: PyObjectId = Field(alias="_id", default=None, serialization_alias="id")
    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "id": "64b9f1f4f1d2b2a3c4e5f6a7",
                "institucion": "Colegio",
                "tipo": "Alimentacion",
                "descripcion": "Factura por alimentacion: empanadas [x10]",
                "total": 100.0,
                "notificar": False,
                "correo": "",
            }
        },
    )


class FacturaCollection(BaseModel):
    # A collection of places
    facturas: List[FacturaOut] = Field(...)