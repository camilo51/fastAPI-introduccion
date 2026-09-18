from fastapi import APIRouter, HTTPException, Query, Depends, Path
from app.schemas.user_schema import UserCreate, UserResponse, UserUpdate
from app.models.user import User
from app.security import generar_hash_contrasena, obtener_usuario_actual
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from database import get_db

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.post("/", response_model=UserResponse, status_code=201)
def crear_usuario(data: UserCreate, db: Session = Depends(get_db)):
    nuevo_usuario = User(
        name=data.name,
        email=data.email,
        password_hash=generar_hash_contrasena(data.password),
        role=data.role,
        is_active=data.is_active
    )

    db.add(nuevo_usuario)

    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=409,
            detail="El correo electrónico ya está registrado"
        )

    db.refresh(nuevo_usuario)

    return nuevo_usuario

@router.get("/", response_model=list[UserResponse])
def obtener_usuarios(
    role: str | None = Query(default=None),
    is_active: bool | None = Query(default=None),
    db: Session = Depends(get_db),
    _usuario_actual: User = Depends(obtener_usuario_actual),
):

    usuarios = db.query(User).all()

    if role is not None:
        usuarios = [
            usuario for usuario in usuarios
            if usuario.role == role
        ]

    if is_active is not None:
        usuarios = [
            usuario for usuario in usuarios
            if usuario.is_active == is_active
        ]

    if not usuarios:
        raise HTTPException(
            status_code=404,
            detail="No se encontraron usuarios"
        )

    return usuarios

@router.get("/{id}", response_model=UserResponse)
def obtener_usuario(
    id: int = Path(..., gt=0),
    db: Session = Depends(get_db),
    _usuario_actual: User = Depends(obtener_usuario_actual),
):
    usuario = db.query(User).get(id)
    if not usuario:
        raise HTTPException(
            status_code=404,
            detail="Usuario no encontrado"
        )
    return usuario

@router.put("/{id}", response_model=UserResponse)
def actualizar_usuario(
    usuario: UserCreate,
    id: int = Path(..., gt=0),
    db: Session = Depends(get_db),
    _usuario_actual: User = Depends(obtener_usuario_actual),
):
    usuario_existente = obtener_usuario(id, db)

    usuario_existente.name = usuario.name
    usuario_existente.email = usuario.email
    usuario_existente.password_hash = generar_hash_contrasena(usuario.password)
    usuario_existente.role = usuario.role
    usuario_existente.is_active = usuario.is_active

    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=409,
            detail="El correo electrónico ya está registrado"
        )
    db.refresh(usuario_existente)

    return usuario_existente

@router.patch("/{id}", response_model=UserResponse)
def actualizar_usuario_parcial(
    usuario: UserUpdate,
    id: int = Path(..., gt=0),
    db: Session = Depends(get_db),
    _usuario_actual: User = Depends(obtener_usuario_actual),
):
    if not usuario.model_dump(exclude_unset=True):
        raise HTTPException(
            status_code=400,
            detail="Debe enviar al menos un campo para actualizar"
        )

    usuario_existente = obtener_usuario(id, db)

    if usuario.name is not None:
        usuario_existente.name = usuario.name

    if usuario.email is not None:
        usuario_existente.email = usuario.email

    if usuario.password is not None:
        usuario_existente.password_hash = generar_hash_contrasena(usuario.password)

    if usuario.role is not None:
        usuario_existente.role = usuario.role

    if usuario.is_active is not None:
        usuario_existente.is_active = usuario.is_active

    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=409,
            detail="El correo electrónico ya está registrado"
        )
    db.refresh(usuario_existente)

    return usuario_existente

@router.delete("/{id}")
def eliminar_usuario(
    id: int = Path(..., gt=0),
    db: Session = Depends(get_db),
    _usuario_actual: User = Depends(obtener_usuario_actual),
):
    usuario_existente = obtener_usuario(id, db)
    db.delete(usuario_existente)
    db.commit()

    return {"message": "Usuario eliminado"}
