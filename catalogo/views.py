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
    html_a_mostrar = (
        "inicio_navidad.html" if datetime.datetime.now().month >= 11 else "inicio.html"
    )
    return render(request, html_a_mostrar)


def lista(request, almacen):
    html_a_mostrar = (
        "base_navidad.html" if datetime.datetime.now().month >= 11 else "base.html"
    )
    return render(request, html_a_mostrar, {"almacen": almacen})


def referencias_genericas(request, almacen, grupo=None, subgrupo=None):
    """
    Vista genérica para manejar referencias según grupo o subgrupo.
    """
    if request.method == "POST":
        color = request.POST.get("color")
        if color == "0":
            if grupo:
                referencias = WpDisponibles.objects.filter(
                    grupo__in=grupo if isinstance(grupo, list) else [grupo],
                    bodega=mi_diccionario[almacen],
                )
            elif subgrupo:
                referencias = WpDisponibles.objects.filter(
                    subgrupo=subgrupo, bodega=mi_diccionario[almacen]
                )
        else:
            if grupo:
                referencias = WpDisponibles.objects.filter(
                    grupo__in=grupo if isinstance(grupo, list) else [grupo],
                    bodega=mi_diccionario[almacen],
                    color=color,
                )
            elif subgrupo:
                referencias = WpDisponibles.objects.filter(
                    subgrupo=subgrupo, bodega=mi_diccionario[almacen], color=color
                )
    else:
        if grupo:
            referencias = WpDisponibles.objects.filter(
                grupo__in=grupo if isinstance(grupo, list) else [grupo],
                bodega=mi_diccionario[almacen],
            )
        elif subgrupo:
            referencias = WpDisponibles.objects.filter(
                subgrupo=subgrupo, bodega=mi_diccionario[almacen]
            )

    for referencia in referencias:
        referencia.tallas_format = (
            referencia.tallas.split("-") if referencia.tallas else ""
        )

    # Colores disponibles
    colores = WpDisponibles.objects.all().values("color").distinct()
    # Paginación
    page = request.GET.get("page", 1)  # Obtener el número de página desde la URL
    paginator = Paginator(referencias, 16)  # Mostrar 16 elementos por página
    referencias_paginadas = paginator.get_page(page)

    # Si es una solicitud AJAX, devolver solo los datos paginados
    if request.headers.get("x-requested-with") == "XMLHttpRequest":
        return render(
            request,
            "partials/referencias_list.html",  # Un archivo parcial para los datos
            {"referencias": referencias_paginadas},
        )

    # Si no es AJAX, devolver la página completa
    return render(
        request,
        "referencias.html",
        {"referencias": referencias_paginadas, "colores": colores},
    )
