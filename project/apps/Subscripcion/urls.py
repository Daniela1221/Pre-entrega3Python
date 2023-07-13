from django.urls import path
from .views import home, subscriptores

app_name = "Subscripcion"

urlpatterns = [
    path("", home, name="home"),
    path("SUBSCRIPCIONES/",subscriptores, name="subscriptores")

]