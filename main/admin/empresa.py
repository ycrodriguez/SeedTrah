from django.contrib import admin
from main.models import Empresa


@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    search_fields = ['codigo', 'nombre', 'direccion', 'telefono']
    list_display = ['codigo', 'nombre', 'direccion', 'telefono']
