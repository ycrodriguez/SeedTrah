from django.contrib import admin
from main.models import Semilla


@admin.register(Semilla)
class SemillaAdmin(admin.ModelAdmin):
    search_fields = ['codigo', 'nombre']
    list_display = ['codigo', 'nombre']
