from django.db import models

# Create your models here.

class TipoLiteratura(models.Model):
    """Tipo de obra literaria: comic, libro, etc"""
    comic_libro = models.CharField(max_length=50,unique=True)

    def __str__(self) -> str:
        return self.comic_libro
    
    class Meta:
        verbose_name = "Tipo de literatura"
        verbose_name_plural = "Tipos de literaturas"

class Libreria(models.Model):
    """Ingreso de libro/comic con sus respectivos detalles"""
    nombre = models.CharField(max_length=50)
    autor = models.CharField(max_length=50)
    tipo = models.ForeignKey(TipoLiteratura,on_delete=models.SET_NULL, null=True, blank=True)
    descripcion = models.TextField(max_length=500)

    def __str__(self) -> str:
        return f"{self.nombre}, {self.autor}"