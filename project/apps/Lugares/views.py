from django.shortcuts import render
from .models import Lugar

# Create your views here.
def home(request):
    registro_lugares = Lugar.objects.all()
    contexto = {"Lugares":registro_lugares}
    return render(request, "Lugares/index_lugares.html",contexto)