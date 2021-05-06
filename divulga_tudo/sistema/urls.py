from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("ad", views.ad, name="ad"),
    path("client", views.client, name="client"),
    path("report", views.report, name="report"),
]