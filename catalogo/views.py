from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from catalogo.models import *
from django.db.models import Q
from django.conf import settings
from django.contrib.auth.models import User, Permission, ContentType, Group
from django.contrib.auth.decorators import login_required
import datetime
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.


class CustomDict(dict):
    def __missing__(self, key):
        return "04"


# Crear un diccionario personalizado
mi_diccionario = CustomDict(
    {
        "pereira": "04",
        "americas": "PA",
        "tulua": "TU",
        "palmira": "PL",
        "pasto": "UP",
    }
)


def catalogo(request):
    return render(request, "inicio.html")


def lista(request, almacen):
    return render(request, "base.html", {"almacen": almacen})


def camisas(request, almacen):
    if request.method == "POST":
        color = request.POST.get("color")
        if color == "0":
            referencias = WpDisponibles.objects.filter(
                grupo="01", bodega=mi_diccionario[almacen]
            )
        else:
            referencias = WpDisponibles.objects.filter(
                grupo="01", bodega=mi_diccionario[almacen], color=color
            )
    else:
        referencias = WpDisponibles.objects.filter(
            grupo="01", bodega=mi_diccionario[almacen]
        )
    for referencia in referencias:
        referencia.tallas_format = (
            referencia.tallas.split("-") if referencia.tallas else ""
        )
    colores = WpDisponibles.objects.all().values("color").distinct()
    return render(
        request, "referencias.html", {"referencias": referencias, "colores": colores}
    )


def pantalones(request, almacen):
    if request.method == "POST":
        color = request.POST.get("color")
        if color == "0":
            referencias = WpDisponibles.objects.filter(
                grupo="02", bodega=mi_diccionario[almacen]
            )
        else:
            referencias = WpDisponibles.objects.filter(
                grupo="02", bodega=mi_diccionario[almacen], color=color
            )
    else:
        referencias = WpDisponibles.objects.filter(
            grupo="02", bodega=mi_diccionario[almacen]
        )
    for referencia in referencias:
        referencia.tallas_format = (
            referencia.tallas.split("-") if referencia.tallas else ""
        )
    colores = WpDisponibles.objects.all().values("color").distinct()
    return render(
        request, "referencias.html", {"referencias": referencias, "colores": colores}
    )


def jeans(request, almacen):
    if request.method == "POST":
        color = request.POST.get("color")
        if color == "0":
            referencias = WpDisponibles.objects.filter(
                grupo="35", bodega=mi_diccionario[almacen]
            )
        else:
            referencias = WpDisponibles.objects.filter(
                grupo="35", bodega=mi_diccionario[almacen], color=color
            )
    else:
        referencias = WpDisponibles.objects.filter(
            grupo="35", bodega=mi_diccionario[almacen]
        )
    for referencia in referencias:
        referencia.tallas_format = (
            referencia.tallas.split("-") if referencia.tallas else ""
        )
    colores = WpDisponibles.objects.all().values("color").distinct()
    return render(
        request, "referencias.html", {"referencias": referencias, "colores": colores}
    )


def camisetas(request, almacen):
    if request.method == "POST":
        color = request.POST.get("color")
        if color == "0":
            referencias = WpDisponibles.objects.filter(
                grupo__in=["03", "60", "30"],
                bodega=mi_diccionario[almacen],
                color=color,
            )
        else:
            referencias = WpDisponibles.objects.filter(
                grupo__in=["03", "60", "30"],
                bodega=mi_diccionario[almacen],
                color=color,
            )
    else:
        referencias = WpDisponibles.objects.filter(
            grupo__in=["03", "60", "30"], bodega=mi_diccionario[almacen]
        )
    for referencia in referencias:
        referencia.tallas_format = (
            referencia.tallas.split("-") if referencia.tallas else ""
        )
    colores = WpDisponibles.objects.all().values("color").distinct()
    return render(
        request, "referencias.html", {"referencias": referencias, "colores": colores}
    )


def bermudas(request, almacen):
    if request.method == "POST":
        color = request.POST.get("color")
        if color == "0":
            referencias = WpDisponibles.objects.filter(
                grupo="04", bodega=mi_diccionario[almacen]
            )
        else:
            referencias = WpDisponibles.objects.filter(
                grupo="04", bodega=mi_diccionario[almacen], color=color
            )
    else:
        referencias = WpDisponibles.objects.filter(
            grupo="04", bodega=mi_diccionario[almacen]
        )
    for referencia in referencias:
        referencia.tallas_format = (
            referencia.tallas.split("-") if referencia.tallas else ""
        )
    colores = WpDisponibles.objects.all().values("color").distinct()
    return render(
        request, "referencias.html", {"referencias": referencias, "colores": colores}
    )


def calzados(request, almacen):
    if request.method == "POST":
        color = request.POST.get("color")
        if color == "0":
            referencias = WpDisponibles.objects.filter(
                grupo__in=["10", "1A", "1L", "70"], bodega=mi_diccionario[almacen]
            )
        else:
            referencias = WpDisponibles.objects.filter(
                grupo__in=["10", "1A", "1L", "70"],
                bodega=mi_diccionario[almacen],
                color=color,
            )
    else:
        referencias = WpDisponibles.objects.filter(
            grupo__in=["10", "1A", "1L", "70"], bodega=mi_diccionario[almacen]
        )
    for referencia in referencias:
        referencia.tallas_format = (
            referencia.tallas.split("-") if referencia.tallas else ""
        )
    colores = WpDisponibles.objects.all().values("color").distinct()
    return render(
        request, "referencias.html", {"referencias": referencias, "colores": colores}
    )


def blazers(request, almacen):
    if request.method == "POST":
        color = request.POST.get("color")
        if color == "0":
            referencias = WpDisponibles.objects.filter(
                grupo__in=["21", "18"], bodega=mi_diccionario[almacen]
            )
        else:
            referencias = WpDisponibles.objects.filter(
                grupo__in=["21", "18"], bodega=mi_diccionario[almacen], color=color
            )
    else:
        referencias = WpDisponibles.objects.filter(
            grupo__in=["21", "18"], bodega=mi_diccionario[almacen]
        )
    for referencia in referencias:
        referencia.tallas_format = (
            referencia.tallas.split("-") if referencia.tallas else ""
        )
    colores = WpDisponibles.objects.all().values("color").distinct()
    return render(
        request, "referencias.html", {"referencias": referencias, "colores": colores}
    )


def vestidos(request, almacen):
    if request.method == "POST":
        color = request.POST.get("color")
        if color == "0":
            referencias = WpDisponibles.objects.filter(
                grupo="22", bodega=mi_diccionario[almacen]
            )
        else:
            referencias = WpDisponibles.objects.filter(
                grupo="22", bodega=mi_diccionario[almacen], color=color
            )
    else:
        referencias = WpDisponibles.objects.filter(
            grupo="22", bodega=mi_diccionario[almacen]
        )
    for referencia in referencias:
        referencia.tallas_format = (
            referencia.tallas.split("-") if referencia.tallas else ""
        )
    colores = WpDisponibles.objects.all().values("color").distinct()
    return render(
        request, "referencias.html", {"referencias": referencias, "colores": colores}
    )


def otros(request, almacen):
    if request.method == "POST":
        color = request.POST.get("color")
        if color == "0":
            referencias = WpDisponibles.objects.filter(
                Q(grupo="CRR"), bodega=mi_diccionario[almacen]
            )
        else:
            referencias = WpDisponibles.objects.filter(
                grupo="CRR", bodega=mi_diccionario[almacen], color=color
            )
    else:
        referencias = WpDisponibles.objects.filter(
            Q(grupo="CRR"), bodega=mi_diccionario[almacen]
        )
    for referencia in referencias:
        referencia.tallas_format = (
            referencia.tallas.split("-") if referencia.tallas else ""
        )
    colores = WpDisponibles.objects.all().values("color").distinct()
    return render(
        request, "referencias.html", {"referencias": referencias, "colores": colores}
    )


def cubaveras(request, almacen):
    if request.method == "POST":
        color = request.POST.get("color")
        if color == "0":
            referencias = WpDisponibles.objects.filter(
                subgrupo="0118", bodega=mi_diccionario[almacen]
            )
        else:
            referencias = WpDisponibles.objects.filter(
                subgrupo="0118", bodega=mi_diccionario[almacen], color=color
            )
    else:
        referencias = WpDisponibles.objects.filter(
            subgrupo="0118", bodega=mi_diccionario[almacen]
        )
    for referencia in referencias:
        referencia.tallas_format = (
            referencia.tallas.split("-") if referencia.tallas else ""
        )
    colores = WpDisponibles.objects.all().values("color").distinct()
    return render(
        request, "referencias.html", {"referencias": referencias, "colores": colores}
    )


def buzos(request, almacen):
    if request.method == "POST":
        color = request.POST.get("color")
        if color == "0":
            referencias = WpDisponibles.objects.filter(
                subgrupo="6003", bodega=mi_diccionario[almacen]
            )
        else:
            referencias = WpDisponibles.objects.filter(
                subgrupo="6003", bodega=mi_diccionario[almacen], color=color
            )
    else:
        referencias = WpDisponibles.objects.filter(
            subgrupo="6003", bodega=mi_diccionario[almacen]
        )
    for referencia in referencias:
        referencia.tallas_format = (
            referencia.tallas.split("-") if referencia.tallas else ""
        )
    colores = WpDisponibles.objects.all().values("color").distinct()
    return render(
        request, "referencias.html", {"referencias": referencias, "colores": colores}
    )
