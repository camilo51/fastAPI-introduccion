# Repositorio de proyectos

Repositorio personal de aprendizaje y desarrollo. Aquí se irán incorporando diferentes proyectos, ejercicios y experimentos organizados en carpetas independientes.

Cada proyecto puede tener su propio lenguaje, herramientas, dependencias y documentación. Consulta el `README.md` dentro de la carpeta correspondiente para conocer sus instrucciones específicas.

## Proyectos

### [`devise_systems/`](devise_systems/)

API REST de gestión de usuarios construida con Python, FastAPI y Pydantic.

Incluye endpoints para:

- Consultar usuarios.
- Filtrar por rol y estado.
- Consultar un usuario por ID.
- Registrar nuevos usuarios.

La aplicación utiliza actualmente una lista en memoria como almacenamiento temporal. Para conocer los requisitos, la instalación, la ejecución y los endpoints disponibles, consulta [`devise_systems/README.md`](devise_systems/README.md).

## Estructura del repositorio

```text
.
├── devise_systems/       # Proyecto actual
│   ├── app/              # Código de la aplicación
│   ├── images/           # Evidencias y recursos del proyecto
│   └── README.md         # Documentación específica
└── README.md             # Documentación general del repositorio
```

Esta estructura crecerá a medida que se agreguen nuevos proyectos. Cada carpeta de primer nivel debe mantenerse independiente y contar con documentación propia cuando requiera instrucciones particulares.

## Convenciones para nuevos proyectos

- Crear una carpeta propia en la raíz del repositorio.
- Añadir un `README.md` con descripción, requisitos, instalación, ejecución y ejemplos.
- Mantener el código, recursos y configuración dentro de la carpeta del proyecto.
- Evitar mezclar dependencias o archivos de configuración entre proyectos.
- Actualizar la sección **Proyectos** de este README al agregar una nueva carpeta.

## Autor

Cristian Camilo Pereira Florez  
Repositorio de aprendizaje y desarrollo, SENA ADSO.
