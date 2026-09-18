from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from pwdlib import PasswordHash
from sqlalchemy.orm import Session

from app.models.user import User
from database import get_db


seguridad_basica = HTTPBasic(realm="device_systems")
hash_contrasena = PasswordHash.recommended()


def generar_hash_contrasena(contrasena: str) -> str:
    """Genera un hash seguro para almacenar la contraseña."""
    return hash_contrasena.hash(contrasena)


def verificar_contrasena(contrasena: str, password_hash: str) -> bool:
    """Comprueba una contraseña contra el hash almacenado."""
    return hash_contrasena.verify(contrasena, password_hash)


def obtener_usuario_actual(
    credenciales: HTTPBasicCredentials = Depends(seguridad_basica),
    db: Session = Depends(get_db),
) -> User:
    """Valida las credenciales HTTP Basic y devuelve el usuario activo."""
    email = credenciales.username.strip().lower()
    usuario = db.query(User).filter(User.email == email).first()

    if (
        usuario is None
        or usuario.password_hash is None
        or not verificar_contrasena(credenciales.password, usuario.password_hash)
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales inválidas",
            headers={"WWW-Authenticate": "Basic"},
        )

    if not usuario.is_active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="El usuario se encuentra inactivo",
        )

    return usuario
