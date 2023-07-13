from django.contrib import admin

# Register your models here.
from . import models

admin.site.site_title = "Lugares Temáticos"

@admin.register(models.Lugar)
class PersonajesAdmin(admin.ModelAdmin):
    list_display = ("nombre", "ciudad","pais") 
    list_filter = ("nombre","ciudad","pais")
    search_fields = ("nombre", )
    ordering = ("nombre",)

@admin.register(models.Ciudad)
class PersonajesAdmin(admin.ModelAdmin):
    ordering = ("nombre",)

@admin.register(models.Pais)
class PersonajesAdmin(admin.ModelAdmin):
    ordering = ("nombre",)