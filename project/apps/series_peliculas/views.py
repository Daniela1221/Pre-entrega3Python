from django.shortcuts import render
from .models import ObraCinematográfica

# Create your views here.
def home(request):
    registro_obras = ObraCinematográfica.objects.all()
    contexto = {"Obras":registro_obras}
    return render(request,"series_peliculas/index_series_peliculas.html",contexto)
