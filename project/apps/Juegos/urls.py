from django.urls import path
from .views import home

app_name = "Juegos"

urlpatterns = [
    path("", home, name="home"),

]