from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("cadastrar_anuncio", views.cadastrar_anuncio, name="cadastrar_anuncio"),
    path("cadastrar_cliente", views.cadastrar_cliente, name="cadastrar_cliente"),
    path("relatorio", views.relatorio, name="relatorio"),
]