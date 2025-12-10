# maintenance/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    EmpresaViewSet, EquipoViewSet, TecnicoViewSet, 
    PlanMantencionViewSet, OrdenTrabajoViewSet, status_check_endpoint
)

# Crea un Router para manejar automáticamente las rutas de ViewSets (list, detail, etc.)
router = DefaultRouter()
router.register(r'companies', EmpresaViewSet)
router.register(r'equipments', EquipoViewSet)
router.register(r'technicians', TecnicoViewSet)
router.register(r'maintenance-plans', PlanMantencionViewSet)
router.register(r'work-orders', OrdenTrabajoViewSet)

urlpatterns = [
    # Incluye las rutas generadas por el Router
    path('', include(router.urls)), 

    # Ruta para el Endpoint de Estado
    path('status/', status_check_endpoint, name='api-status'),
]