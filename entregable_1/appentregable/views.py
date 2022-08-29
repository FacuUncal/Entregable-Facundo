from django.shortcuts import render
from .models import Familia
from django.http import HttpResponse

from django.template import loader

# Create your views here.



def familia(request):
    
    mama = Familia(nombre='Sandra', apellido='Amerio', edad=57, telefono=11552899, email='sandra@gmail.com',nacimiento= '1965-10-2')
    papa = Familia(nombre='Alejandro', apellido='Uncal', edad=62, telefono=11778812, email='ale@gmail.com', nacimiento= '1960-10-22')
    hermana = Familia(nombre='Lucia', apellido='Uncal Amerio', edad=25, telefono=11664459, email='lucia@gmail.com', nacimiento= '1995-12-4')
    mama.save()
    papa.save()
    hermana.save()
    texto_m =f'Hola mi nombre es {mama.nombre} y mi apellido es {mama.apellido}. Tengo {mama.edad}, naci en el año {mama.nacimiento}. Mi telefono es {mama.telefono} y mi email es {mama.email}'#
    texto_p =f'Hola mi nombre es {papa.nombre} y mi apellido es {papa.apellido}. Tengo {papa.edad}, naci en el año {papa.nacimiento}. Mi telefono es {papa.telefono} y mi email es {papa.email}'#
    texto_h =f'Hola mi nombre es {hermana.nombre} y mi apellido es {hermana.apellido}. Tengo {hermana.edad}, naci en el año {hermana.nacimiento}. Mi telefono es {hermana.telefono} y mi email es {hermana.email}'#
    
    diccionario = {'texto_h':texto_h,'texto_m':texto_m,'texto_p':texto_p}
    
    plantilla=loader.get_template("plantilla_1.html")

    documento=plantilla.render(diccionario)
    return HttpResponse(documento)

