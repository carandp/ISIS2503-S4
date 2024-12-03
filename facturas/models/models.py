# Models for the facturas microservice

import uuid
from enum import Enum
from bson import ObjectId
from pydantic import BaseModel, Field, ConfigDict
from typing import List
from models.db import PyObjectId


class FacturaType(str, Enum):
    Alimentacion = "alimentacion"
    Transporte = "transporte"
    Otro = "otro"


class Factura(BaseModel):
    descripcion: str = Field(...)
    tipo: FacturaType = Field(...)
    total: float = Field(...)
    notificar: bool = Field(default=False)
    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
        json_schema_extra={
            "example": {
                "descripcion": "Factura por alimentacion: empanadas [x10]",
                "tipo": FacturaType.Alimentacion,
                "total": 100.0,
                "notificar": False,
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
                "descripcion": "Factura por alimentacion: empanadas [x10]",
                "tipo": FacturaType.Alimentacion,
                "total": 100.0,
                "notificar": False,
            }
        },
    )


class FacturaCollection(BaseModel):
    # A collection of places
    facturas: List[FacturaOut] = Field(...)