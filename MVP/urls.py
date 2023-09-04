from django.contrib import admin
from django.urls import path, include
from . import views
from .views import *
from django.contrib.auth.views import LogoutView
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),

    #petsitters
    path('petsitters/', views.petsitters, name='petsitters'),
    path('agregar_cuidador/', views.agregar_cuidador, name='agregar_cuidador'),
    path('editar_cuidador/<int:cuidador_id>/', views.editar_cuidador, name='editar_cuidador'),
    path('eliminar_cuidador/<int:cuidador_id>/', views.eliminar_cuidador, name='eliminar_cuidador'),
    path('buscar_cuidador/', views.buscar_cuidador, name='buscar_cuidador'),

    #mascostas
    path('mascotas/', views.MascotaList.as_view(), name='mascotas'),
    path('agregar_mascota/', views.MascotaCreate.as_view(), name='agregar_mascota'),
    path('update_mascota/<int:pk>/', views.MascotaUpdate.as_view(), name='update_mascota'),
    path('deleted_mascota/<int:pk>/', views.MascotaDelete.as_view(), name='deleted_mascota'),
   
    #petowners
    path('petowners/', views.DuenoMascotaList.as_view(), name='petowners'),
    path('agregar_dueno/', views.DuenoMascotaCreate.as_view(), name='agregar_dueno'),
    path('update_dueno/<int:pk>/', views.DuenoMascotaUpdate.as_view(), name='update_dueno'),
    path('deleted_dueno/<int:pk>/', views.DuenoMascotaDelete.as_view(), name='deleted_dueno'),

    #autentificación
    path('register/', views.register, name='registro'),
    path('login/', views.login_request, name='login'),
    path('logout/', LogoutView.as_view(template_name="logout.html"), name='logout'),
    path('editarperfil/', views.editarPerfil, name='editarperfil'),

    #otras paginas
    path('acerca_de_mi/', TemplateView.as_view(template_name="acerca_de_mi.html"), name='acerca_de_mi'),
]