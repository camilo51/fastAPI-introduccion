# Repositorio de proyectos

Repositorio personal de aprendizaje y desarrollo. Cada proyecto se encuentra en una carpeta independiente y puede tener su propio código, dependencias, recursos y documentación.

## Proyectos actuales

### [`devise_systems/`](devise_systems/)

API REST de gestión de usuarios desarrollada con Python, FastAPI, Pydantic, SQLAlchemy y SQLite.

La documentación específica para descargar, instalar y ejecutar este proyecto se encuentra en [`devise_systems/README.md`](devise_systems/README.md).

## Estructura general del repositorio

```text
FASTAPI/
├── .git/                         # Metadatos y control de versiones de Git
├── README.md                     # Documentación general del repositorio
└── devise_systems/               # Proyecto de API REST
    ├── app/                      # Código fuente de la aplicación
    │   ├── main.py               # Punto de entrada de FastAPI
    │   ├── models/               # Modelos de base de datos SQLAlchemy
    │   │   ├── curso.py
    │   │   ├── inscripcion.py
    │   │   └── user.py
    │   ├── routes/               # Endpoints de la API
    │   │   ├── curso_routes.py
    │   │   └── user_routes.py
    │   └── schemas/              # Validación de datos con Pydantic
    │       ├── curso_schema.py
    │       └── user_schema.py
    ├── images/                   # Capturas y evidencias de pruebas
    ├── database.py               # Conexión y sesiones de SQLite
    ├── requirements.txt          # Dependencias de Python
    ├── .gitignore                # Archivos excluidos de Git
    └── README.md                 # Documentación del proyecto
```

## Función de cada carpeta

### `devise_systems/`

Contiene el proyecto de la API. Tiene su propia configuración, dependencias y documentación.

### `devise_systems/app/`

Contiene el código principal de la aplicación FastAPI.

### `devise_systems/app/models/`

Contiene los modelos que representan las tablas de la base de datos: usuarios, cursos e inscripciones.

### `devise_systems/app/routes/`

Contiene las rutas HTTP organizadas por funcionalidad. Actualmente las rutas de usuarios están implementadas; el archivo de rutas de cursos está reservado para una ampliación futura.

### `devise_systems/app/schemas/`

Contiene los esquemas Pydantic que definen y validan la información que recibe y devuelve la API.

### `devise_systems/images/`

Contiene evidencias visuales de las pruebas realizadas con los endpoints y sus validaciones.

## Archivos de configuración

- `database.py`: configura SQLAlchemy y la base de datos SQLite local.
- `requirements.txt`: lista las librerías necesarias para el proyecto.
- `.gitignore`: evita que archivos locales, entornos virtuales y caché se suban a Git.

## Archivos generados localmente

Al instalar o ejecutar el proyecto pueden aparecer archivos que no forman parte del código fuente, por ejemplo:

- `.venv/`: entorno virtual de Python.
- `__pycache__/`: caché de Python.
- `test.db`: base de datos SQLite local.
- Archivos de log o configuraciones locales.

Estos archivos deben permanecer excluidos mediante `.gitignore` cuando corresponda.

## Organización para nuevos proyectos

Para agregar otro proyecto al repositorio:

1. Crear una carpeta nueva en la raíz.
2. Mantener dentro de ella su código, recursos y archivos de configuración.
3. Crear un README propio con la descripción y las instrucciones del proyecto.
4. Agregar el nuevo proyecto a la sección **Proyectos** de este README.
5. Evitar mezclar dependencias o bases de datos entre proyectos.

## Autor

Cristian Camilo Pereira Florez  
Repositorio de aprendizaje y desarrollo para el programa ADSO del SENA.
