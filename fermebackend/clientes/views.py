from django.shortcuts import render, redirect
from django.contrib.auth import logout, update_session_auth_hash

from clientes.forms import RegistroForm, EditarCuentaForm

from django.contrib.auth.forms import PasswordChangeForm

from django.http import JsonResponse

import json

from home.models import Producto
from clientes.models import *


def registro(response):
    if response.method == "POST":
        form = RegistroForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = RegistroForm()

    return render(response, "clientes/registro.html", {"form": form})


def logout_view(request):
    redirect("clientes/registration/logout.html")
    logout(request)


def editarCuenta(request):
    if request.method == "POST":
        form = EditarCuentaForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = EditarCuentaForm(instance=request.user)
        return render(request, 'clientes/editar_cuenta.html', {"form": form})


def cambiarPassword(request):
    if request.method == "POST":
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/')
        else:
            form = redirect('/clientes/cambiar_password')
    else:
        form = PasswordChangeForm(user=request.user)
        return render(request, 'clientes/cambiar_password.html',
                      {"form": form})


def checkout(request):
    # if request.user.is_authenticated:
    #     cliente = request.user
    #     orden, created = Orden.object.get_or_create(cliente=cliente,
    #                                                 complete=False)
    #     productos = orden.ordenproducto_set.all()
    # else:
    #     productos = []
    #     orden = {'get_cart_total': 0, 'get_cart_items': 0}

    # context = {'productos': productos, 'orden': orden}

    return render(request, 'clientes/checkout.html', context)


def actualizarProducto(request):
    body_unicode = request.body.decode('utf-8')
    data = json.loads(body_unicode)

    idProducto = data['idProducto']
    accion = data['accion']

    print('idProducto:', idProducto)
    print('accion:', accion)

    cliente = request.user
    producto = Producto.objects.get(id_producto=idProducto)
    orden, created = Orden.objects.get_or_create(cliente=cliente,
                                                 finalizada=False)
    ordenProducto, created = OrdenProducto.objects.get_or_create(
        orden=orden, producto=producto)

    if accion == 'agregar':
        ordenProducto.cantidad = (ordenProducto.cantidad + 1)
    elif accion == 'eliminar':
        ordenProducto.cantidad = (ordenProducto.cantidad - 1)

    ordenProducto.save()

    if ordenProducto.cantidad <= 0:
        ordenProducto.delete()

    return JsonResponse('Producto agregado', safe=False)


def carro(request):

    if request.user.is_authenticated:
        cliente = request.user
        orden, created = Orden.objects.get_or_create(cliente=cliente,
                                                     finalizada=False)
        productos = orden.ordenproducto_set.all()
    else:
        productos = []

    context = {'productos': productos, 'orden': orden}

    return render(request, 'clientes/carro.html', context)
