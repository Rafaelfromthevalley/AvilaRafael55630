from MVP import *
from django.shortcuts import render
from django.http import HttpResponse
#from .views import agregar_dueno

def home(request):
    contexto = {
        'titulo': 'Pet Sitter para tus mascotas',}
    return render(request, 'base.html', contexto)

#def home(request):
        #return render(request, "MVP/home.html")