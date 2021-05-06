from django.contrib import messages
from django.shortcuts import render

from .models import Client, Ad

def index(request):
    return render(request, "sistema/index.html")

def ad(request):
    return render(request, "sistema/ad.html")

def client(request):
    if request.method == 'POST':
        name = request.POST['name']

        if not name:
            messages.error(request, f"Nome inválido.")
            return render(request, "sistema/client.html")

        # Checks if client's name is already registered
        try:
            Client.objects.get(name=name)
            messages.error(request, f"Nome já cadastrado.")
            return render(request, "sistema/client.html")
        except Client.DoesNotExist:
            pass
        
        # Attempts to register new client to database
        try:
            new_client = Client(name=name)
            new_client.save()
            messages.error(request, f"Cadastro efetuado com sucesso.")
        except Exception:
            messages.error(request, f"Cadastro não efetuado.")
            return render(request, "sistema/client.html")

    return render(request, "sistema/client.html")

def report(request):
    return render(request, "sistema/report.html")