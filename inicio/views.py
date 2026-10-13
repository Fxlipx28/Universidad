from django.shortcuts import render


def home(request):
    contexto = {
        "titulo": "Proyecto Universidad",
        "integrantes": ["Felipe", "Compañero 2", "Compañero 3"],
    }
    return render(request, "inicio/home.html", contexto)


def crear_salida(request):
    contexto = {
        "titulo": "Nueva Salida",
    }
    return render(request, "inicio/crear_salida.html", contexto)