from django.urls import path
from .views import home

app_name = "series_peliculas"

urlpatterns = [
    path("", home, name="home"),

]