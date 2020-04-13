from django.shortcuts import render
from django.http import HttpResponse


def login(request):
    return HttpResponse('pag de login')


def registro(request):
    return HttpResponse('pag de regitro')

# def perfil(request):
#     return HttpResponse('perfil')
