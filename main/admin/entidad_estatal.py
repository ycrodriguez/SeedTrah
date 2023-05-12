from django.contrib import admin
from main.models import EntidadEstatal


@admin.register(EntidadEstatal)
class EntidadEstatalAdmin(admin.ModelAdmin):
    search_fields = ['numero_inscripcion', 'tipo']
    list_display = ['numero_inscripcion', 'tipo']
