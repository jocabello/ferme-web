from django.shortcuts import render
from django.http import HttpResponse
from clientes.models import Cliente
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import redirect


def home(request):
    return render(request, 'home/home.html')


def home_test(request):
    context = {}
    clientes = Cliente.objects.all()
    context['clientes'] = clientes

    return render(request, 'personal/home', context)


def contacto(request):
    if request.method == 'POST':
        msj = request.POST.get('mensaje')
        nom = request.POST.get('nombre')
        correo = request.POST.get('email')
        send_mail(
            'CONTACTO-WEB',
            'NOMBRE: ' + nom + ' CORREO: ' + correo + ' MENSAJE: ' + msj,
            correo,
            [settings.EMAIL_HOST_USER],
            fail_silently=False,
        )
        return redirect('/')
    return render(request, 'home/contacto.html')


def proveedor(request):
    if request.method == 'POST':
        nom = request.POST.get('nombre')
        msj = request.POST.get('mensaje')
        correo = request.POST.get('email')
        num = request.POST.get('fono')
        empresa = request.POST.get('nombreEmpresa')
        send_mail(
            'PROVEEDOR',
            'NOMBRE: ' + nom + ' CORREO: ' + correo + ' FONO: ' + num +
            ' EMPRESA: ' + empresa + ' MENSAJE: ' + msj,
            correo,
            [settings.EMAIL_HOST_USER],
            fail_silently=False,
        )
        return redirect('/')
    return render(request, 'home/proveedor.html')
