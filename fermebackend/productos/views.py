from django.shortcuts import render
from django.http import HttpResponse
from django.db import models
from home import models  # intellisense mala en VScode


def catalogo(request):
    productos = models.Producto.objects.all()
    tipos = models.TipoProduct.objects.all()
    familias = models.FamilyProduct.objects.all()

    contexto = {'tipos': tipos, 'familias': familias, 'productos': productos}

    return render(request, 'productos/catalogo.html', contexto)


def detalle(request, id):
    producto = models.Producto.objects.get(id_producto=id)
    tipos = models.TipoProduct.objects.all()
    familias = models.FamilyProduct.objects.all()

    contexto = {'tipos': tipos, 'familias': familias, 'producto': producto}

    return render(request, 'productos/detalle.html', contexto)


def obtener_datos_producto(id):
    producto = models.Producto.objects.get(id_producto=id)
    tipo = models.TipoProduct.objects.get(id_family=producto.fk_id_product)
    familia = models.FamilyProduct.objects.all(
        id_family=producto.fk_id_familia)

    return {'tipo': tipo, 'familia': familia}
