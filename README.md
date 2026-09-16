# Sistema de Gestión de Tickets

Aplicación web desarrollada con Django para la gestión y seguimiento de tickets de soporte.

## Descripción

El sistema permite autenticar usuarios, registrar tickets de soporte, consultar su información detallada y gestionar su estado en una plataforma web responsiva.

La aplicación utiliza Django como framework backend, SQLite como base de datos ligera de desarrollo, WhiteNoise para archivos estáticos y Gunicorn/Render para despliegue en producción.

## Tecnologías utilizadas

* Python 3.12+
* Django 4.2+
* SQLite3
* Gunicorn
* WhiteNoise
* HTML5 / CSS3 / JavaScript

## Funcionalidades

* Autenticación de usuarios (Inicio de sesión y cierre de sesión protegidos).
* Crear y registrar nuevos tickets de soporte.
* Consultar el listado completo de tickets.
* Consultar el detalle individual de cada ticket.
* Población automática de datos iniciales/usuarios mediante comandos personalizados.
* Administrar registros mediante el panel de administración de Django.

## Requisitos

Antes de ejecutar el proyecto se necesita tener instalado:

* Python 3.12 o compatible (>= 3.10).
* Pip (Gestor de paquetes de Python).
* Git (Opcional, para clonación del repositorio).
* Visual Studio Code (Recomendado).

## Instalación

### 1. Descargar o clonar el proyecto

Ubicar el proyecto en una carpeta de trabajo o clonarlo mediante Git:

git clone https://github.com/aepenaranda02-glitch/prueba.git
cd prueba

### 2. Abrir la carpeta en Visual Studio Code

Abrir la carpeta raíz `prueba` que contiene el archivo `manage.py`.

### 3. Crear y activar el entorno virtual

Crear un entorno virtual aislado para instalar las dependencias:

* En Windows:
  python -m venv venv
  venv\Scripts\activate

* En Linux / macOS:
  python3 -m venv venv
  source venv/bin/activate

### 4. Instalar dependencias del proyecto

Ejecutar en la terminal el siguiente comando para instalar Django, WhiteNoise y Gunicorn:

pip install -r requirements.txt

## Configuración de la base de datos

El proyecto utiliza SQLite por defecto, por lo que no requiere la instalación ni configuración de un servidor de base de datos externo. La configuración de conexión local se encuentra en:

config/settings.py

## Migraciones y Datos Iniciales (Seed)

Para estructurar la base de datos y cargar automáticamente los datos y usuarios iniciales de prueba, ejecuta en orden:

# Aplicar migraciones del sistema
python manage.py migrate

# Cargar usuarios por defecto para pruebas rápidas
python manage.py create_default_users

## Ejecutar el proyecto

Desde la carpeta donde se encuentra manage.py, ejecutar:

python manage.py runserver

Luego abrir en el navegador web la siguiente dirección:

http://127.0.0.1:8000/

## Panel de administración

El proyecto cuenta con el panel administrativo de Django:

http://127.0.0.1:8000/admin/

Para acceder o gestionar superusuarios, puedes crear una cuenta administradora ejecutando:

python manage.py createsuperuser

## Estructura principal

prueba/
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── tickets/
│   ├── management/
│   │   └── commands/
│   │       └── create_default_users.py
│   ├── migrations/
│   ├── static/
│   ├── templates/
│   ├── admin.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── build.sh
├── manage.py
├── README.md
├── requirements.txt
└── runtime.txt

## Despliegue en la Nube (Render / Railway)

El proyecto incluye archivos listos para producción (build.sh, runtime.txt y gunicorn):

1. Build Command: ./build.sh
2. Start Command: gunicorn config.wsgi:application

## Autor

Proyecto desarrollado como parte de una prueba/práctica de desarrollo de software por Ángel Peñaranda.
