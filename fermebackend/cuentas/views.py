from django.shortcuts import render
from django.http import HttpResponse


def login(request):
    return render(request, 'cuentas/login.html')


def registro(request):
    return render(request, 'cuentas/registro.html')

# def perfil(request):
#     return HttpResponse('perfil')
