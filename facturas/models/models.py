# Models for the facturas microservice

import uuid
from enum import Enum
from pydantic import BaseModel, Field, ConfigDict
from typing import List
from models.db import PyObjectId


class FacturaType(str, Enum):
    Alimentacion = "alimentacion"
    Transporte = "transporte"
    Otro = "otro"


class Factura(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    descripcion: str = Field(...)
    tipo: FacturaType = Field(...)
    total: float = Field(...)
    notificar: bool = Field(default=False)
    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
        json_schema_extra={
            "example": {
                "id": "1",
                "descripcion": "Factura por alimentacion: empanadas [x10]",
                "tipo": FacturaType.Alimentacion,
                "total": 100.0,
                "notificar": False,
            }
        },
    )


class FacturaOut(Factura):
    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "id": "1",
                "descripcion": "Factura por alimentacion: empanadas [x10]",
                "tipo": FacturaType.Alimentacion,
                "total": 100.0,
                "notificar": False,
            }
        },
    )


class FacturaCollection(BaseModel):
    # A collection of places
    places: List[FacturaOut] = Field(...)