from django.contrib import admin

# Register your models here.
from . import models

admin.site.site_title = "Juegos"

@admin.register(models.Juego)
class PersonajesAdmin(admin.ModelAdmin):
    list_display = ("nombre", "direccion_url") 
    list_filter = ("nombre",)
    search_fields = ("nombre", )
    ordering = ("nombre",)

