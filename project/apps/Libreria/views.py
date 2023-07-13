from django.shortcuts import render
from .models import Libreria
# Create your views here.
def home(request):
    registro_libreria = Libreria.objects.all()
    contexto = {"Literatura":registro_libreria}
    return render(request, "Libreria/index_libreria.html",contexto)