from django.db import models

# Create your models here.

class TipoCinematográfico(models.Model):
    """Crea un tipo se obra cinematográfica, ya sea serie, película, etc"""
    nombre = models.CharField(max_length=50, verbose_name="Nombre del Tipo Cinematográfico")

    def __str__(self) -> str:
        return self.nombre
    
    class Meta:
        verbose_name = "Tipo Cinematográfico"
        verbose_name_plural = "Tipos Cinematográficos"

class ObraCinematográfica(models.Model):
    """Ingreso de película, serie, etc"""
    nombre = models.CharField(max_length=50, verbose_name="Nombre Obra")
    tipo = models.ForeignKey(TipoCinematográfico,on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Tipo Cinematográfico")
    fecha = models.CharField(max_length=10, verbose_name="Año de estreno")
    descripcion = models.TextField(max_length=1000,verbose_name="Descripción")

    def __str__(self):
        return f"{self.nombre}, {self.tipo}, {self.fecha}"
    
    class Meta:
        verbose_name = "Obra Cinematográfica"
        verbose_name_plural = "Obras Cinematográficas"
