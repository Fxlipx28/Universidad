from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("crear-salida/", views.crear_salida, name="crear_salida"),
]