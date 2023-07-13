from django.shortcuts import render
from .models import Juego

# Create your views here.
def home(request):
    registro_juegos = Juego.objects.all()
    contexto = {"Juegos":registro_juegos}
    return render(request, "Juegos/index_juegos.html",contexto)