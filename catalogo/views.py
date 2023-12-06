from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.shortcuts import get_object_or_404, render,redirect
from catalogo.models import *
from django.db.models import Q
from django.conf import settings
from django.contrib.auth.models import User,Permission,ContentType,Group
from django.contrib.auth.decorators import login_required
import datetime
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

class CustomDict(dict):
    def __missing__(self, key):
        return '04'

# Crear un diccionario personalizado
mi_diccionario = CustomDict({
    'pereira': '04',
    'americas': 'PA',
    'tulua': 'TU',
    'palmira': 'PL',
    'pasto': 'UP',
})

def catalogo(request):
    return render(request,'inicio_navidad.html')

def lista(request, almacen):   
    return render(request,'base_navidad.html' ,{'almacen':almacen})

def camisas(request, almacen):
    print(mi_diccionario[almacen])
    referencias= WpDisponibles.objects.filter(grupo='01', bodega = mi_diccionario[almacen])
    for referencia in referencias:
        referencia.tallas_format = referencia.tallas.split('-') if referencia.tallas else ''
    return render(request,'referencias.html',{'referencias':referencias})

def pantalones(request, almacen):
    referencias= WpDisponibles.objects.filter(grupo='02', bodega = mi_diccionario[almacen])
    for referencia in referencias:
        referencia.tallas_format = referencia.tallas.split('-') if referencia.tallas else ''
    return render(request,'referencias.html',{'referencias':referencias})


def jeans(request, almacen):
    referencias= WpDisponibles.objects.filter(grupo='35', bodega = mi_diccionario[almacen])
    for referencia in referencias:
        referencia.tallas_format = referencia.tallas.split('-') if referencia.tallas else ''    
    return render(request,'referencias.html',{'referencias':referencias})


def camisetas(request , almacen):
    referencias= WpDisponibles.objects.filter(grupo__in=['03','60','30'], bodega = mi_diccionario[almacen])
    for referencia in referencias:
        referencia.tallas_format = referencia.tallas.split('-') if referencia.tallas else ''
    return render(request,'referencias.html',{'referencias':referencias})

def bermudas(request, almacen):
    referencias= WpDisponibles.objects.filter(grupo='04', bodega = mi_diccionario[almacen])
    for referencia in referencias:
        referencia.tallas_format = referencia.tallas.split('-') if referencia.tallas else ''
    return render(request,'referencias.html',{'referencias':referencias})

def calzados(request, almacen):
    referencias= WpDisponibles.objects.filter(grupo__in=['10','1A','1L','70'], bodega = mi_diccionario[almacen])
    for referencia in referencias:
        referencia.tallas_format = referencia.tallas.split('-') if referencia.tallas else ''
    return render(request,'referencias.html',{'referencias':referencias})

def blazers(request, almacen):
    referencias= WpDisponibles.objects.filter(grupo__in=['21','18'], bodega = mi_diccionario[almacen])
    for referencia in referencias:
        referencia.tallas_format = referencia.tallas.split('-') if referencia.tallas else ''
    return render(request,'referencias.html',{'referencias':referencias})

def vestidos(request, almacen):
    referencias= WpDisponibles.objects.filter(grupo='22', bodega = mi_diccionario[almacen])
    for referencia in referencias:
        referencia.tallas_format = referencia.tallas.split('-') if referencia.tallas else ''
    return render(request,'referencias.html',{'referencias':referencias})

def otros(request, almacen):
    referencias= WpDisponibles.objects.filter(Q(grupo='CRR'), bodega = mi_diccionario[almacen])
    for referencia in referencias:
        referencia.tallas_format = referencia.tallas.split('-') if referencia.tallas else ''
    return render(request,'referencias.html',{'referencias':referencias})

def cubaveras(request, almacen):
    referencias= WpDisponibles.objects.filter(subgrupo='0118',  bodega = mi_diccionario[almacen])
    for referencia in referencias:
        referencia.tallas_format = referencia.tallas.split('-') if referencia.tallas else ''
    return render(request,'referencias.html',{'referencias':referencias})

def buzos(request, almacen):
    referencias= WpDisponibles.objects.filter(subgrupo='6003', bodega = mi_diccionario[almacen])
    for referencia in referencias:
        referencia.tallas_format = referencia.tallas.split('-') if referencia.tallas else ''
    return render(request,'referencias.html',{'referencias':referencias})