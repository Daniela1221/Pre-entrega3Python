from django.contrib import admin

# Register your models here.
from . import models

admin.site.site_title = "Librería"

@admin.register(models.Libreria)
class PersonajesAdmin(admin.ModelAdmin):
    list_display = ("nombre", "autor","tipo") 
    list_filter = ("nombre","tipo")
    search_fields = ("nombre", )
    ordering = ("nombre",)

@admin.register(models.TipoLiteratura)
class PersonajesAdmin(admin.ModelAdmin):
    ordering = ("comic_libro",)