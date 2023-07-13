from django.urls import path
from .views import home

app_name = "Lugares"

urlpatterns = [
    path("", home, name="home"),

]