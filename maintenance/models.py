from django.db import models
from django.contrib.auth.models import User

# --- 1. EMPRESA ---
class Empresa(models.Model):
    # Atributos básicos requeridos
    name = models.CharField(max_length=100, unique=True, verbose_name="Nombre")
    rut = models.CharField(max_length=12, unique=True, verbose_name="RUT") 
    address = models.CharField(max_length=200, blank=True, null=True, verbose_name="Dirección") 
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")

    def __str__(self):
        return self.name

# --- 2. TÉCNICO ---
# Se relaciona 1:1 con un usuario de Django para la autenticación
class Tecnico(models.Model):
    # Relación 1:1 con User (un usuario es un técnico, y un técnico es un usuario)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, verbose_name="Usuario") 
    full_name = models.CharField(max_length=150, verbose_name="Nombre Completo") 
    specialty = models.CharField(max_length=100, verbose_name="Especialidad") 
    phone = models.CharField(max_length=15, blank=True, null=True, verbose_name="Teléfono") 
    def __str__(self):
        return self.full_name

# --- 3. EQUIPO ---
class Equipo(models.Model):
    # Relación N:1 (ForeignKey): Muchos equipos pertenecen a una Empresa
    company = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name='equipos', verbose_name="Empresa Cliente") 
    name = models.CharField(max_length=100, verbose_name="Nombre del Equipo") 
    serial_number = models.CharField(max_length=50, unique=True, verbose_name="Número de Serie")
    critical = models.BooleanField(default=False, verbose_name="Equipo Crítico")
    installed_at = models.DateField(verbose_name="Fecha de Instalación") 

    def __str__(self):
        return f"{self.name} ({self.serial_number})"

# --- 4. PLAN DE MANTENCIÓN ---
class PlanMantencion(models.Model):
    # Relación N:1: Varios planes pueden asociarse al mismo Equipo
    equipment = models.ForeignKey(Equipo, on_delete=models.CASCADE, related_name='planes', verbose_name="Equipo Asociado") 
    name = models.CharField(max_length=100, verbose_name="Nombre del Plan") 
    frequency_days = models.PositiveIntegerField(verbose_name="Frecuencia (días)") 
    active = models.BooleanField(default=True, verbose_name="Activo") 

    def __str__(self):
        return f"Plan: {self.name}"

# --- 5. ORDEN DE TRABAJO ---
class OrdenTrabajo(models.Model):
    STATUS_CHOICES = [
        ('PENDIENTE', 'Pendiente'),
        ('EN_PROGRESO', 'En Progreso'),
        ('COMPLETADA', 'Completada'),
        ('CANCELADA', 'Cancelada'),
    ]

    # Relaciones N:1
    plan = models.ForeignKey(PlanMantencion, on_delete=models.SET_NULL, null=True, blank=True, related_name='ordenes', verbose_name="Plan de Mantención")
    equipment = models.ForeignKey(Equipo, on_delete=models.CASCADE, related_name='ordenes_trabajo', verbose_name="Equipo") 
    technician = models.ForeignKey(Tecnico, on_delete=models.SET_NULL, null=True, related_name='ordenes_asignadas', verbose_name="Técnico Asignado") 

    # Atributos
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDIENTE', verbose_name="Estado") 
    scheduled_date = models.DateField(verbose_name="Fecha Programada") 
    completed_at = models.DateTimeField(null=True, blank=True, verbose_name="Fecha de Finalización") 
    notes = models.TextField(blank=True, verbose_name="Notas del Trabajo") 

    def __str__(self):
        return f"OT N°{self.id} - {self.equipment.name}"