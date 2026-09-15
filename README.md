# Sistema de Gestión de Tickets

Aplicación web desarrollada con Django para la gestión y seguimiento de tickets de soporte.

## Descripción

El sistema permite registrar tickets de soporte, consultar su información, gestionar su prioridad y estado, y agregar comentarios relacionados con cada ticket.

La aplicación utiliza Django como framework backend y SQL Server como sistema de gestión de base de datos.

## Tecnologías utilizadas

* Python
* Django
* SQL Server
* Microsoft SQL Server Management Studio (SSMS)
* mssql-django
* pyodbc
* HTML
* CSS
* JavaScript

## Funcionalidades

* Crear tickets.
* Consultar tickets registrados.
* Filtrar tickets por estado.
* Filtrar tickets por prioridad.
* Consultar el detalle de un ticket.
* Cambiar el estado de un ticket.
* Cambiar la prioridad de un ticket.
* Agregar comentarios a los tickets.
* Administrar los registros mediante el panel de administración de Django.

## Requisitos

Antes de ejecutar el proyecto se necesita tener instalado:

* Python 3.13 o compatible.
* Microsoft SQL Server.
* SQL Server Management Studio (SSMS).
* ODBC Driver 18 for SQL Server.
* Visual Studio Code (recomendado).

## Instalación

### 1. Descargar o clonar el proyecto

Ubicar el proyecto en una carpeta de trabajo.

### 2. Abrir la carpeta en Visual Studio Code

Abrir la carpeta que contiene el archivo:

`manage.py`

### 3. Instalar Django

Abrir una terminal dentro de la carpeta del proyecto y ejecutar:

```bash
python -m pip install django
```

### 4. Instalar el conector para SQL Server

Ejecutar:

```bash
python -m pip install mssql-django
```

También se utiliza el controlador:

```text
ODBC Driver 18 for SQL Server
```

## Configuración de la base de datos

El proyecto utiliza una base de datos SQL Server llamada:

```text
Tickets
```

La configuración se encuentra en:

```text
config/settings.py
```

La conexión utilizada para el entorno local es:

```python
DATABASES = {
    'default': {
        'ENGINE': 'mssql',
        'NAME': 'Tickets',
        'HOST': 'localhost',
        'PORT': '',
        'OPTIONS': {
            'driver': 'ODBC Driver 18 for SQL Server',
            'trusted_connection': 'yes',
            'extra_params': 'TrustServerCertificate=yes',
        },
    },
}
```

## Migraciones

Después de configurar la base de datos, ejecutar:

```bash
python manage.py migrate
```

Este comando crea las tablas necesarias en la base de datos.

## Ejecutar el proyecto

Desde la carpeta donde se encuentra `manage.py`, ejecutar:

```bash
python manage.py runserver
```

Luego abrir en el navegador:

```text
http://127.0.0.1:8000/tickets/
```

## Panel de administración

El proyecto también cuenta con el panel administrativo de Django:

```text
http://127.0.0.1:8000/admin/
```

Para utilizarlo se debe crear un usuario administrador con:

```bash
python manage.py createsuperuser
```

## Estructura principal

```text
ANGEL PEÑA/
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── tickets/
│   ├── migrations/
│   ├── templates/
│   ├── admin.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── db.sqlite3
├── manage.py
└── README.md
```

## Base de datos

Las principales entidades utilizadas por el sistema son:

### Ticket

Contiene información como:

* Título
* Descripción
* Categoría
* Prioridad
* Estado
* Fecha de creación
* Fecha de actualización

### Comentario

Permite registrar comentarios asociados a un ticket.

Cada comentario contiene:

* Ticket relacionado
* Título
* Descripción
* Fecha de registro

## Estados de los tickets

El sistema maneja los siguientes estados:

* Abierto
* En proceso
* Resuelto
* Cerrado

## Prioridades

El sistema maneja las siguientes prioridades:

* Baja
* Media
* Alta
* Crítica

## Autor

Proyecto desarrollado como parte de una prueba/práctica de desarrollo de software.

