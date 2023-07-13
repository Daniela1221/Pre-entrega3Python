from django.contrib import admin

# Register your models here.
from . import models

admin.site.site_title = "Cinematrografía"

@admin.register(models.ObraCinematográfica)
class PersonajesAdmin(admin.ModelAdmin):
    list_display = ("nombre", "fecha","tipo") 
    list_filter = ("nombre","fecha","tipo")
    search_fields = ("nombre", )
    ordering = ("nombre",)

@admin.register(models.TipoCinematográfico)
class PersonajesAdmin(admin.ModelAdmin):
    ordering = ("nombre",)
