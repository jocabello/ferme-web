from django.shortcuts import render, redirect
from django.contrib.auth import logout, update_session_auth_hash

from clientes.forms import RegistroForm, EditarCuentaForm

from django.contrib.auth.forms import PasswordChangeForm

from django.http import JsonResponse

import json
import datetime

from home.models import Producto, Venta, TipoVenta, DetalleVenta
from clientes.models import *

from django.contrib.auth.decorators import login_required


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


@login_required
def checkout(request):
    if request.user.is_authenticated:
        cliente = request.user
        orden, created = Orden.objects.get_or_create(cliente=cliente,
                                                     finalizada=False)
        productos = orden.ordenproducto_set.all()
        itemsCarro = Orden.get_items_carro
    else:
        productos = []
        orden = {'get_total_carro': 0, 'get_items_carro': 0}
        itemsCarro = orden['get_items_carro']

    context = {'productos': productos,
               'orden': orden, 'itemsCarro': itemsCarro}

    return render(request, 'clientes/checkout.html', context)


def procesarOrden(request):
    body_unicode = request.body.decode('utf-8')
    data = json.loads(body_unicode)

    print('datos: ', request.body)

    transaccion_id = datetime.datetime.now().timestamp()

    if request.user.is_authenticated:
        cliente = request.user

        asdas = cliente.email
        asdasd = cliente.id

        clienteObjeto = Cliente.objects.get(email=asdas)

        orden, created = Orden.objects.get_or_create(cliente=cliente,
                                                     finalizada=False)
        total = data['total']
        orden.id_transaccion = transaccion_id

        # ordenProducto = OrdenProducto.objects.get(
        #     orden=orden)

        productos = orden.ordenproducto_set.all()

        for i in productos:
            producto = Producto.objects.get(
                id_producto=i.producto.id_producto)
            producto.stock = (producto.stock - i.cantidad)
            producto.save()

        # if total == orden.get_total_carro: #para no manipular desde el front
        orden.finalizada = True
        orden.save()

        DireccionDespacho.objects.create(  # NFRespaldo, enviar correo?quizás SI!
            cliente=cliente,
            orden=orden,
            calle=data['despacho']['calle'],
            numero=data['despacho']['numero'],
            zipcode=data['despacho']['zipcode'],
            comentario=data['despacho']['comentario'],
        )

        if(cliente.tipo_cliente == 'pnatural'):
            tipoVenta = TipoVenta.objects.get(id_tipo_venta=1)  # 1=boleta
        if(cliente.tipo_cliente == 'empresa'):
            tipoVenta = TipoVenta.objects.get(id_tipo_venta=2)  # 2=factura

        # registroVenta = Venta.objects.create(
        #     total=total,
        #     es_nula='n',
        #     tipo_venta_id_tipo_venta=tipoVenta,
        #     cliente_id_cliente=MiCliente.objects.get(email=asdas),
        #     funcionario_rut_funcionario=99999999
        # )
        # registroVenta.save()

        # for i in productos:
        #     registroDetalle = DetalleVenta.objects.create(
        #         cantidad=i.cantidad,
        #         venta_id_venta=registroVenta.id_venta,
        #         producto_id_producto=i.producto.id_producto,
        #         venta_id_tipo_venta=tipoVenta,
        #     )
        #     registroDetalle.save()

    else:
        print("usuario no logueado")
    return JsonResponse('Pago realizado', safe=False)
