"""fermebackend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from clientes.views import registro, logout_view, editarCuenta, cambiarPassword, actualizarProducto, carro, checkout, procesarOrden

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cuentas.urls')),
    path('', include('home.urls')),
    path('', include('productos.urls')),

    #path('', include('clientes.urls')),
    path('registro/', registro, name="registro"),
    path('', include('django.contrib.auth.urls')),
    path('logout/', logout_view, name="logout_view"),
    path('editarcuenta/', editarCuenta, name="editarCuenta"),
    path('cambiarpassword/', cambiarPassword, name="cambiarPassword"),
    path('actualizar_producto/',
         actualizarProducto,
         name="actualizar_producto"),
    path('carro/', carro, name="carro"),
    path('checkout/', checkout, name="checkout"),

    path('procesar_orden/',
         procesarOrden,
         name="procesar_orden"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
