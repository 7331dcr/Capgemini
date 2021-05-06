from django.shortcuts import render

def index(request):
    return render(request, "sistema/index.html")

def ad(request):
    return render(request, "sistema/ad.html")

def client(request):
    return render(request, "sistema/client.html")

def report(request):
    return render(request, "sistema/report.html")