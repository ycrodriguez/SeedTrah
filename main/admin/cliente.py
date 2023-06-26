from django.contrib import admin
from main.models import Cliente, Empresa


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    search_fields = ['nombre', 'direccion', 'telefono']
    list_display = ['nombre', 'direccion', 'telefono', 'tipo', 'persona_natural', 'entidad_estatal']
