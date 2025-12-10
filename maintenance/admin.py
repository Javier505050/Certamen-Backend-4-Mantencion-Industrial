from django.contrib import admin

from django.contrib import admin
from .models import Empresa, Tecnico, Equipo, PlanMantencion, OrdenTrabajo

admin.site.register(Empresa)
admin.site.register(Tecnico)
admin.site.register(Equipo)
admin.site.register(PlanMantencion)
admin.site.register(OrdenTrabajo)