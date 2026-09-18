import logging
from time import perf_counter

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

from app.routes.user_routes import router
from database import create_tables


logger = logging.getLogger("uvicorn.error")


app = FastAPI(
    title="device_systems",
    description="API REST para la gestión de usuarios",
    version="1.0"
)


@app.middleware("http")
async def agregar_cabeceras(request: Request, call_next):
    inicio = perf_counter()

    response = await call_next(request)
    duracion_ms = (perf_counter() - inicio) * 1000

    response.headers["X-App-Name"] = "device_systems"
    response.headers["X-API-Version"] = "1.0"
    response.headers["X-Process-Time-Ms"] = f"{duracion_ms:.2f}"

    logger.info(
        "%s %s -> %s [%.2f ms]",
        request.method,
        request.url.path,
        response.status_code,
        duracion_ms,
    )

    return response


# El ultimo middleware registrado es el mas externo. Asi CORS tambien agrega
# sus cabeceras a las respuestas generadas por el middleware personalizado.
origenes_permitidos = [
    "http://localhost:3000",
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origenes_permitidos,
    allow_credentials=False,
    allow_methods=["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"],
    allow_headers=["Content-Type", "Authorization"],
    expose_headers=["X-App-Name", "X-API-Version", "X-Process-Time-Ms"],
)


app.include_router(router)

create_tables() 
