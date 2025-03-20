"""wp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from catalogo.views import catalogo, lista, referencias_genericas

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", catalogo, name="menu"),
    path("catalogo/<str:almacen>", lista, name="catalogo"),
    path(
        "catalogo/<str:almacen>/camisas/",
        referencias_genericas,
        {"grupo": "01"},
        name="camisas",
    ),
    path(
        "catalogo/<str:almacen>/cubaveras/",
        referencias_genericas,
        {"subgrupo": "0118"},
        name="cubaveras",
    ),
    path(
        "catalogo/<str:almacen>/pantalones/",
        referencias_genericas,
        {"grupo": "02"},
        name="pantalones",
    ),
    path(
        "catalogo/<str:almacen>/jeans/",
        referencias_genericas,
        {"grupo": "35"},
        name="jeans",
    ),
    path(
        "catalogo/<str:almacen>/camisetas/",
        referencias_genericas,
        {"grupo": ["03", "60", "30"]},
        name="camisetas",
    ),
    path(
        "catalogo/<str:almacen>/bermudas/",
        referencias_genericas,
        {"grupo": "04"},
        name="bermudas",
    ),
    path(
        "catalogo/<str:almacen>/calzados/",
        referencias_genericas,
        {"grupo": ["10", "1A", "1L", "70"]},
        name="calzados",
    ),
    path(
        "catalogo/<str:almacen>/blazers/",
        referencias_genericas,
        {"grupo": ["21", "18"]},
        name="blazers",
    ),
    path(
        "catalogo/<str:almacen>/vestidos/",
        referencias_genericas,
        {"grupo": "22"},
        name="vestidos",
    ),
    path(
        "catalogo/<str:almacen>/otros/",
        referencias_genericas,
        {"grupo": "CRR"},
        name="otros",
    ),
    path(
        "catalogo/<str:almacen>/buzos/",
        referencias_genericas,
        {"subgrupo": "6003"},
        name="buzos",
    ),
]
