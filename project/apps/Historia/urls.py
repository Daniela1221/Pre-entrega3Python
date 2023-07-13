from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name = "Historia"

urlpatterns = [
    path("", views.home ,name="home"),
    path("Personaje/list/",views.PersonajeList.as_view(), name = "personaje_list"),
    path("Personaje/create/",views.PersonajeCreate.as_view(), name = "personaje_create"),
    path("Faccion/create/",views.FaccionCreate.as_view(), name = "faccion_create"),
    path("Personaje/detail/<int:pk>",views.PersonajeDetail.as_view(), name = "personaje_detail"),
    path("Personaje/update/<int:pk>",views.PersonajeUpdate.as_view(), name = "personaje_update"),
    path("Personaje/delete/<int:pk>",views.PersonajeDelete.as_view(), name = "personaje_delete"),

]