from django.contrib import admin
from main.models import Almacen


@admin.register(Almacen)
class Almacenadmin(admin.ModelAdmin):
    search_fields = ['codigo', 'nombre', 'capacidad', 'direccion']
    list_display = ['codigo', 'nombre', 'capacidad', 'direccion', 'empresa']
