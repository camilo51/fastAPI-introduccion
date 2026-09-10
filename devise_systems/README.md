# Device Systems

API REST para la gestión de usuarios desarrollada con Python, FastAPI, Pydantic y SQLAlchemy.

Este proyecto forma parte del repositorio de aprendizaje de Cristian Camilo Pereira Florez para el programa de Análisis y Desarrollo de Software del SENA.

## Características

- API construida con FastAPI.
- Documentación automática con Swagger y ReDoc.
- CRUD completo para usuarios.
- Validación de datos con Pydantic.
- Persistencia de usuarios en SQLite mediante SQLAlchemy.
- Filtros de usuarios por rol y estado.
- Control de correo electrónico duplicado.
- Middleware que agrega cabeceras informativas a las respuestas.

## Requisitos

- Python 3.10 o superior.
- Git, para descargar el repositorio.

Las dependencias de Python están definidas en `requirements.txt`.

## Descargar el proyecto

Desde una terminal, ejecuta:

```bash
git clone https://github.com/camilo51/fastAPI-introduccion.git
cd fastAPI-introduccion/devise_systems
```

Si ya descargaste el repositorio, solo debes entrar a la carpeta del proyecto:

```bash
cd devise_systems
```

## Instalación

### Windows PowerShell

Desde la carpeta `devise_systems`, crea un entorno virtual:

```powershell
py -m venv .venv
```

Actívalo:

```powershell
.\.venv\Scripts\Activate.ps1
```

Si PowerShell impide la activación de scripts, puedes ejecutar:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

Instala las dependencias:

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### Linux o macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Ejecutar la aplicación

Con el entorno virtual activo y ubicado en la carpeta `devise_systems`, ejecuta:

```bash
uvicorn app.main:app --reload
```

La API estará disponible en:

```text
http://127.0.0.1:8000
```

Para detener el servidor, presiona `Ctrl + C`.

## Documentación interactiva

FastAPI genera automáticamente las siguientes páginas:

- Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

Desde Swagger UI puedes consultar y probar los endpoints sin utilizar otra herramienta.

## Estructura del proyecto

```text
devise_systems/
├── app/
│   ├── main.py
│   ├── models/
│   │   ├── curso.py
│   │   ├── inscripcion.py
│   │   └── user.py
│   ├── routes/
│   │   ├── curso_routes.py
│   │   └── user_routes.py
│   └── schemas/
│       ├── curso_schema.py
│       └── user_schema.py
├── images/
├── database.py
├── requirements.txt
├── .gitignore
└── README.md
```

### Descripción de los archivos y carpetas

#### `app/main.py`

Es el punto de entrada de la aplicación. Crea la instancia de FastAPI, registra el router de usuarios, configura el middleware y ejecuta la creación de las tablas de la base de datos.

#### `app/routes/user_routes.py`

Contiene las rutas HTTP para crear, consultar, actualizar y eliminar usuarios. El router utiliza el prefijo `/users`.

#### `app/routes/curso_routes.py`

Actualmente está reservado para las rutas de cursos, pero todavía no contiene endpoints y no está registrado en `main.py`.

#### `app/schemas/user_schema.py`

Contiene los esquemas Pydantic utilizados para validar los datos de entrada y salida de usuarios:

- `UserCreate`: datos necesarios para crear un usuario.
- `UserResponse`: estructura de respuesta de un usuario.
- `UserUpdate`: campos opcionales para una actualización parcial.

#### `app/schemas/curso_schema.py`

Contiene los esquemas Pydantic preparados para cursos (`CursoBase`, `CursoCreate` y `Curso`).

#### `app/models/user.py`

Define el modelo SQLAlchemy `User` y la tabla `users` de SQLite.

#### `app/models/curso.py` y `app/models/inscripcion.py`

Definen los modelos SQLAlchemy para cursos e inscripciones. Actualmente son estructuras preparadas para una ampliación futura.

#### `database.py`

Configura SQLAlchemy, la sesión de base de datos y la conexión SQLite. La función `create_tables()` crea las tablas registradas en los modelos.

#### `images/`

Contiene capturas de pantalla de pruebas, validaciones y respuestas de la API.

#### `requirements.txt`

Lista las dependencias necesarias para ejecutar el proyecto:

- `fastapi`
- `uvicorn`
- `email-validator`
- `sqlalchemy`

#### `.gitignore`

Evita subir al repositorio entornos virtuales, caché de Python, configuraciones locales, archivos de IDE y logs.

## Base de datos

La aplicación utiliza SQLite con la configuración definida en `database.py`:

```python
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
```

El archivo `test.db` se crea en la carpeta del proyecto cuando se inicia la aplicación. Las tablas se crean automáticamente mediante `create_tables()`.

La base de datos es local y está destinada al desarrollo. No se utiliza un servidor externo de base de datos.

## Modelo de usuario

| Campo | Tipo | Requerido | Descripción |
|---|---|---:|---|
| `id` | Integer | Sí, automático | Identificador único |
| `name` | String | Sí | Nombre entre 3 y 100 caracteres |
| `email` | Email | Sí | Correo válido, normalizado y único |
| `role` | String | Sí | `admin`, `support` o `user` |
| `is_active` | Boolean | Sí | Estado del usuario |

## Endpoints de usuarios

Todos los endpoints utilizan el prefijo `/users`.

### Crear un usuario

```http
POST /users/
```

Solicitud:

```json
{
  "name": "Laura",
  "email": "laura@gmail.com",
  "role": "user",
  "is_active": true
}
```

Respuesta `201 Created`:

```json
{
  "id": 1,
  "name": "Laura",
  "email": "laura@gmail.com",
  "role": "user",
  "is_active": true
}
```

### Obtener todos los usuarios

```http
GET /users/
```

Admite los filtros opcionales `role` e `is_active`:

```http
GET /users/?role=admin
GET /users/?is_active=true
GET /users/?role=admin&is_active=true
```

### Obtener un usuario por ID

```http
GET /users/{id}
```

Ejemplo:

```http
GET /users/1
```

### Actualizar completamente un usuario

```http
PUT /users/{id}
```

Debe enviar todos los campos del usuario:

```json
{
  "name": "Laura Actualizada",
  "email": "laura.actualizada@gmail.com",
  "role": "support",
  "is_active": true
}
```

### Actualizar parcialmente un usuario

```http
PATCH /users/{id}
```

Solo es necesario enviar los campos que se desean cambiar:

```json
{
  "name": "Laura Modificada"
}
```

### Eliminar un usuario

```http
DELETE /users/{id}
```

Respuesta:

```json
{
  "message": "Usuario eliminado"
}
```

## Validaciones y errores

- `200 OK`: consulta o actualización exitosa.
- `201 Created`: usuario creado correctamente.
- `400 Bad Request`: una actualización parcial no contiene campos.
- `404 Not Found`: usuario no encontrado o no hay usuarios que coincidan con los filtros.
- `409 Conflict`: el correo electrónico ya está registrado.
- `422 Unprocessable Content`: los datos enviados no cumplen las validaciones.

Reglas principales:

- `name` debe tener entre 3 y 100 caracteres. Los espacios al inicio y al final se eliminan.
- `email` debe tener un formato válido. Se guardan los correos sin espacios y en minúscula.
- `role` solo puede ser `admin`, `support` o `user`.
- `is_active` debe ser booleano.
- `email` no puede repetirse.
- El `id` debe ser mayor que cero.
- Un `PATCH` debe enviar al menos un campo para actualizar.

Ejemplo de correo duplicado:

```json
{
  "detail": "El correo electrónico ya está registrado"
}
```

## Cabeceras de respuesta

El middleware de `app/main.py` agrega estas cabeceras a las respuestas:

```text
X-App-Name: device_systems
X-API-Version: 1.0
```

## Estado actual

La funcionalidad de usuarios está conectada a SQLite y cuenta con operaciones CRUD. Los modelos y esquemas de cursos e inscripciones están creados como base para futuras funcionalidades, pero sus endpoints aún están pendientes de implementación.

## Autor

Cristian Camilo Pereira Florez

Ficha: 3223877

Programa: Tecnólogo en Análisis y Desarrollo de Software (ADSO)

SENA - CTMA
