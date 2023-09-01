from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('agregar_cuidador/', views.agregar_cuidador, name='agregar_cuidador'),
    path('agregar_dueno/', views.agregar_dueno, name='agregar_dueno'),
    path('agregar_mascota/', views.agregar_mascota, name='agregar_mascota'),
    path('buscar_cuidador/', views.buscar_cuidador, name='buscar_cuidador'),
]