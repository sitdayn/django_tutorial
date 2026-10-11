from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('vsem_privet', views.vsem_privet, name="vsem_privet"),
    path
]
