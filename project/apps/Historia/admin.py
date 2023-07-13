from django.contrib import admin

# Register your models here.
from . import models

admin.site.site_title = "Personajes"

@admin.register(models.Personaje)
class PersonajesAdmin(admin.ModelAdmin):
    list_display = ("nombre", "faccion") 
    list_filter = ("nombre","faccion")
    search_fields = ("nombre", )
    ordering = ("nombre",)

@admin.register(models.Faccion)
class PersonajesAdmin(admin.ModelAdmin):
    ordering = ("nombre",)