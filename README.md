# API RESTful para Mantención Industrial - INACAP T13041

## 1. Descripción
Este proyecto es la Evaluación N°4 de Programación Backend y consiste en el desarrollo de una API RESTful con Django REST Framework para gestionar empresas clientes, equipos, técnicos, planes de mantención y órdenes de trabajo. [cite_start]La autenticación se realiza mediante JWT. [cite: 134]

## 2. Requisitos y Dependencias
* Python 3.x
* [cite_start]Dependencias principales: [cite: 135]
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
3.  **Aplicar migraciones y crear superusuario:** [cite: 136]
    ```bash
    python manage.py migrate
    python manage.py createsuperuser
    ```
4.  **Ejecutar el servidor:** [cite: 136]
    ```bash
    python manage.py runserver
    ```

## 4. Endpoints de la API
[cite_start]La API opera bajo la ruta base `/api/`. [cite: 137]

| URL | Método | Descripción | Requiere Autenticación |
| :--- | :--- | :--- | :--- |
| `/api/status/` | GET | Valida que la API esté en línea y conectada a la DB. | NO |
| `/api/companies/` | GET | Listado de empresas clientes. | NO (solo lectura) |
| `/api/companies/` | POST | Crear una nueva empresa cliente. | SÍ |
| `/api/token/` | POST | Obtener Token JWT (Access y Refresh). | NO |
