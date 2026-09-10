from pydantic import BaseModel, Field, field_validator
from datetime import datetime
from typing import Optional

class CursoBase(BaseModel):
    nombre: str = Field(..., min_length=3, max_length=100)
    descripcion: Optional[str] = Field(None, max_length=300)
    horas: int = Field(0, ge=0, le=500)
    activo: bool = True

    @field_validator("nombre")
    @classmethod
    def nombre_sin_espacios_extra(cls, v: str) -> str:
        return v.strip()

class CursoCreate(CursoBase):
    pass

class Curso(CursoBase):
    id: int
    creado_en: datetime

    class Config:
        from_attributes = True