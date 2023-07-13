from django.urls import path
from .views import home

app_name = "Libreria"

urlpatterns = [
    path("", home, name="home"),

]