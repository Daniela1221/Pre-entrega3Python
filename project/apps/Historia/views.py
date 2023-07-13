from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView, DetailView, UpdateView
from django.urls import reverse_lazy
from . import forms, models

def home(request):
    query = models.Personaje.objects.all()
    contexto = {"datos_registro":query}
    return render(request,"Historia/index_historia.html",contexto)


#Listar todos los Personajes
class PersonajeList(ListView):  
    model = models.Personaje

#Crear Personaje
class PersonajeCreate(CreateView):
    model = models.Personaje
    form_class = forms.PersonajeForm
    success_url = reverse_lazy("Historia:personaje_list")
    
#Crear Faccion
class FaccionCreate(CreateView):
    model = models.Faccion
    form_class = forms.FaccionForm
    success_url = reverse_lazy("Historia:personaje_create")

#Ver más detalles de Personaje
class PersonajeDetail(DetailView):
    model = models.Personaje

#Actualizar datos de Personaje
class PersonajeUpdate(UpdateView):
    model = models.Personaje
    form_class = forms.PersonajeForm
    success_url = reverse_lazy("Historia:personaje_list")

#Eliminar datos de Personaje
class PersonajeDelete(DeleteView):
    model = models.Personaje
    success_url = reverse_lazy("Historia:personaje_list")


