from django.shortcuts import render
from django.http import HttpResponse
from django.db import models
from home import models  # intellisense mala en VScode


def tipoProducto(producto):
    tipos = models.Tipo_Product.objects.all()
    return 0

def catalogo(request):
    productos = models.Producto.objects.all()
    return render(request, 'productos/catalogo.html', {'productos': productos})


def detalle(request):
    return render(request, 'productos/detalle.html', {})


# TODO en home, hacer template genérico de login, logout, registro, recuperación de contraseña, etc, que sea consumido por las apps
# TODO app admins
# TODO app clientes (natural o empresa)
# TODO app proveedores