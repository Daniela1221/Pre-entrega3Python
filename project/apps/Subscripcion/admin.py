from django.contrib import admin

# Register your models here.
from . import models

admin.site.site_title = "Subscripciones"


@admin.register(models.Subscribete)
class PersonajesAdmin(admin.ModelAdmin):
    list_display = ("nombre", "apellido","correo") 
    list_filter = ("nombre","apellido","correo")
    search_fields = ("nombre", )
    ordering = ("nombre",)