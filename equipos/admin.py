from django.contrib import admin
from .models import Equipo

# Register your models here.

@admin.register(Equipo)
class EquipoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'estado', 'fecha_ingreso', 'ubicacion')
    list_filter = ('categoria', 'estado')
    search_fields = ('nombre', 'ubicacion')