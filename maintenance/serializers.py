# maintenance/serializers.py

from rest_framework import serializers
from .models import Empresa, Equipo, Tecnico, PlanMantencion, OrdenTrabajo
from django.contrib.auth.models import User

# Serializer para el usuario de Django (necesario para el modelo Tecnico)
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name')


# 1. EMPRESA
class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = '__all__' # Incluye todos los campos del modelo

# 2. TÉCNICO
class TecnicoSerializer(serializers.ModelSerializer):
    # Muestra los detalles del usuario relacionado en lugar de solo el ID
    user_details = UserSerializer(source='user', read_only=True) 

    class Meta:
        model = Tecnico
        fields = '__all__'

# 3. EQUIPO
class EquipoSerializer(serializers.ModelSerializer):
    # Muestra solo el nombre de la empresa, no todos los detalles (opcional, pero mejora la legibilidad)
    company_name = serializers.ReadOnlyField(source='company.name')

    class Meta:
        model = Equipo
        fields = '__all__'

# 4. PLAN DE MANTENCIÓN
class PlanMantencionSerializer(serializers.ModelSerializer):
    equipment_name = serializers.ReadOnlyField(source='equipment.name')

    class Meta:
        model = PlanMantencion
        fields = '__all__'

# 5. ORDEN DE TRABAJO
class OrdenTrabajoSerializer(serializers.ModelSerializer):
    technician_name = serializers.ReadOnlyField(source='technician.full_name')

    class Meta:
        model = OrdenTrabajo
        fields = '__all__'