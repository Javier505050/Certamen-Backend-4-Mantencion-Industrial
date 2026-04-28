# API RESTful para Mantención Industrial

## 1. Descripción
Este proyecto consiste en el desarrollo de una API RESTful con Django REST Framework para gestionar empresas clientes, equipos, técnicos, planes de mantención y órdenes de trabajo.La autenticación se realiza mediante JWT.

## 2. Requisitos y Dependencias
* Python 3.x
* Dependencias principales: 
    * `Django`
    * `djangorestframework`
    * `djangorestframework-simplejwt`
    
## 3. Pasos para la Ejecución
1.  **Crear y activar el entorno virtual:**
    ```bash
    python -m venv venv
    .\venv\Scripts\activate
    ```
2.  **Instalar dependencias:**
    ```bash
    pip install -r requirements.txt # O usar el listado de dependencias
    ```
3.  **Aplicar migraciones y crear superusuario:** 
    ```bash
    python manage.py migrate
    python manage.py createsuperuser
    ```
4.  **Ejecutar el servidor:** 
    ```bash
    python manage.py runserver
    ```

## 4. Endpoints de la API
La API opera bajo la ruta base `/api/`. 

| URL | Método | Descripción | Requiere Autenticación |
| :--- | :--- | :--- | :--- |
| `/api/status/` | GET | Valida que la API esté en línea y conectada a la DB. | NO |
| `/api/companies/` | GET | Listado de empresas clientes. | NO (solo lectura) |
| `/api/companies/` | POST | Crear una nueva empresa cliente. | SÍ |
| `/api/token/` | POST | Obtener Token JWT (Access y Refresh). | NO |
