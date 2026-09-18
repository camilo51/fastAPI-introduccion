from datetime import datetime
from pydantic import BaseModel, ConfigDict, EmailStr, Field, field_validator
from typing import Literal


class UserBase(BaseModel):
    name: str = Field(..., min_length=3, max_length=100)
    email: EmailStr
    role: Literal["admin", "support", "user"]
    is_active: bool

    @field_validator("name", mode="before")
    @classmethod
    def validar_nombre(cls, value):
        if not isinstance(value, str):
            raise ValueError("El nombre debe ser texto")

        value = value.strip()

        if len(value) < 3:
            raise ValueError("El nombre debe tener mínimo 3 caracteres")

        if len(value) > 100:
            raise ValueError("El nombre no puede tener más de 100 caracteres")

        return value

    @field_validator("email", mode="before")
    @classmethod
    def normalizar_email(cls, value):
        if isinstance(value, str):
            return value.strip().lower()
        return value

class UserCreate(UserBase):
    password: str = Field(..., min_length=8, max_length=128)

    @field_validator("password")
    @classmethod
    def validar_contrasena(cls, value):
        if len(value) < 8:
            raise ValueError("La contraseña debe tener mínimo 8 caracteres")
        return value

class UserResponse(UserBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
    created_at: datetime

class UserUpdate(BaseModel):
    name: str | None = Field(None, min_length=3, max_length=100)
    email: EmailStr | None = None
    password: str | None = Field(None, min_length=8, max_length=128)
    role: Literal["admin", "support", "user"] | None = None
    is_active: bool | None = None

    @field_validator("name", mode="before")
    @classmethod
    def validar_nombre(cls, value):
        if value is None:
            return value

        if not isinstance(value, str):
            raise ValueError("El nombre debe ser texto")

        value = value.strip()

        if len(value) < 3:
            raise ValueError("El nombre debe tener mínimo 3 caracteres")

        if len(value) > 100:
            raise ValueError("El nombre no puede tener más de 100 caracteres")

        return value

    @field_validator("email", mode="before")
    @classmethod
    def normalizar_email(cls, value):
        if isinstance(value, str):
            return value.strip().lower()
        return value

    @field_validator("password")
    @classmethod
    def validar_contrasena(cls, value):
        if value is None:
            return value

        if len(value) < 8:
            raise ValueError("La contraseña debe tener mínimo 8 caracteres")
        return value
