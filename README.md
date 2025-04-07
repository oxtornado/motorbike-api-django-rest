# 🏍️ MOTOS API

API REST desarrollada con **Django** y **Django REST Framework** para gestionar información sobre motocicletas.

## 📌 Objetivo

Crear una aplicación backend que provea datos por medio de una API web.

## ⚙️ Tecnologías

- Python 3.x
- Django
- Django REST Framework
- SQLite
- CORS Headers

## 📁 Estructura del Proyecto

```bash
app_motos/
├── app_motos/
│   ├── settings.py
│   └── urls.py
├── motos_api/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
└── manage.py
```

## 🚀 Instalación

1. Crea un entorno virtual:
   ```bash
   python -m venv env
   source env/bin/activate  # En Linux/Mac
   env\Scripts\activate     # En Windows
   ```

2. Instala Django y dependencias:
   ```bash
   pip install django djangorestframework django-cors-headers
   ```

3. Crea el proyecto y la app:
   ```bash
   django-admin startproject app_motos
   cd app_motos
   python manage.py startapp motos_api
   ```

4. Agrega en `settings.py`:
   ```python
   INSTALLED_APPS = [
       ...
       'rest_framework',
       'corsheaders',
       'motos_api',
   ]
   ```

5. Configura el modelo `Moto` en `motos_api/models.py`:
   ```python
   class Moto(models.Model):
       reference = models.CharField(max_length=100)
       trademark = models.CharField(max_length=100)
       model = models.IntegerField()
       price = models.FloatField()
       image = models.URLField()
       supplier = models.CharField(max_length=100)
   ```

6. Realiza migraciones:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

7. Crea superusuario:
   ```bash
   python manage.py createsuperuser
   ```

8. Corre el servidor:
   ```bash
   python manage.py runserver
   ```

## 🔗 Endpoints

| Método | URL                         | Descripción                            |
|--------|-----------------------------|----------------------------------------|
| GET    | `/api/`                     | Lista todas las motos                  |
| POST   | `/api/`                     | Agrega una nueva moto                  |
| GET    | `/api/<int:id>/`           | Obtiene una moto por su ID             |
| PUT    | `/api/<int:id>/`           | Actualiza una moto                     |
| DELETE | `/api/<int:id>/`           | Elimina una moto                       |

## 📦 Exportar e importar dependencias

Para guardar las dependencias:
```bash
pip freeze > requirements.txt
```

Para instalarlas en otro entorno:
```bash
pip install -r requirements.txt
```

## 👤 Made By Oxtornado

Este proyecto es parte de una guía educativa para el desarrollo de APIs con Django REST Framework.
