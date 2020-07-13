from django.shortcuts import render
from django.http import HttpResponse
from clientes.models import Cliente
from django.core.mail import send_mail
from django.conf import settings


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
        correo = request.POST.get('email')
        num = request.POST.get('fono')
        send_mail(
            'CONTACTO-WEB',
            'CORREO: ' + correo + ' FONO: ' + num + ' MENSAJE: ' + msj,
            correo,
            [settings.EMAIL_HOST_USER],
            fail_silently=False,
        )
    return render(request, 'home/contacto.html')
