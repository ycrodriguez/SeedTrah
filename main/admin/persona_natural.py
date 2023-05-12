from django.contrib import admin
from main.models import PersonaNatural


@admin.register(PersonaNatural)
class PersonaNaturalAdmin(admin.ModelAdmin):
    search_fields = ['ci']
    list_display = ['ci']
