from django.db import models

# Create your models here.

class Pais(models.Model):
    """País para mencionar donde se encuentra el lugar temático"""
    nombre = models.CharField(max_length=50,unique=True)

    def __str__(self) -> str:
        return self.nombre
    class Meta:
        verbose_name = "País"
        verbose_name_plural = "Países"
    
class Ciudad(models.Model):
    """Ciudad para mencionar donde se encuentra el lugar temático"""
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self) -> str:
        return self.nombre
    
    class Meta:
        verbose_name = "Ciudad"
        verbose_name_plural = "Ciudades"

class Lugar(models.Model):
    """Creación de un lugar temático"""
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    ciudad = models.ForeignKey(Ciudad,on_delete=models.SET_NULL, null=True, blank=True)
    pais = models.ForeignKey(Pais,on_delete=models.SET_NULL, null=True, blank=True)
    descripcion = models.TextField(max_length=500)

    def __str__(self) -> str:
        return self.nombre
    
    class Meta:
        verbose_name = "Lugar Temático"
        verbose_name_plural = "Lugares Temáticos"

