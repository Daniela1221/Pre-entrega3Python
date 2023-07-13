from django.db import models

# Create your models here.

class Subscribete(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.correo}"
    
    class Meta:
        verbose_name = "Subscripción"
        verbose_name_plural = "Subscripciones"
