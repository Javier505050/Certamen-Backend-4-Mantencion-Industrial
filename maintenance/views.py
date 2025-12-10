from django.shortcuts import render

# Create your views here.
# maintenance/views.py

from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated

from .models import Empresa, Equipo, Tecnico, PlanMantencion, OrdenTrabajo
from .serializers import (
    EmpresaSerializer, EquipoSerializer, TecnicoSerializer, 
    PlanMantencionSerializer, OrdenTrabajoSerializer
)

# ----------------------------------------------------------------------
# VISTAS CRUD (Requerimiento 4: API RESTful completa)
# ModelViewSet genera automáticamente GET (lista y detalle), POST, PUT, DELETE
# ----------------------------------------------------------------------

class EmpresaViewSet(viewsets.ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer

class EquipoViewSet(viewsets.ModelViewSet):
    queryset = Equipo.objects.all()
    serializer_class = EquipoSerializer

class TecnicoViewSet(viewsets.ModelViewSet):
    # Opcional: solo permitir que se vean los técnicos activos
    queryset = Tecnico.objects.all() 
    serializer_class = TecnicoSerializer

class PlanMantencionViewSet(viewsets.ModelViewSet):
    queryset = PlanMantencion.objects.all()
    serializer_class = PlanMantencionSerializer

class OrdenTrabajoViewSet(viewsets.ModelViewSet):
    queryset = OrdenTrabajo.objects.all()
    serializer_class = OrdenTrabajoSerializer


# ----------------------------------------------------------------------
# ENDPOINT DE ESTADO (Requerimiento 3.1.3 Endpoint de estado)
# ----------------------------------------------------------------------
@api_view(['GET'])
@permission_classes([AllowAny]) # Permitir el acceso a cualquiera, incluso no autenticados
def status_check_endpoint(request):
    """
    Endpoint para validar la disponibilidad general de la API. 
    """
    # Intentar acceder a la base de datos para verificar la conectividad
    try:
        Empresa.objects.exists()
        db_status = "OK"
    except Exception as e:
        db_status = f"Error DB: {str(e)}"

    return Response({
        "status": "online",
        "service": "Industrial Maintenance API",
        "db_connection": db_status,
        "api_version": "v1",
        "message": "La API está disponible y entregando datos en JSON."
    }, status=status.HTTP_200_OK)