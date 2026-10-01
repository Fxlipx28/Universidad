from django.shortcuts import render

def home(request):
    contexto = {
        "titulo": "Proyecto Universidad",
        "integrantes": ["Felipe", "Compañero 2", "Compañero 3"],
    }
    return render(request, "inicio/home.html", contexto)