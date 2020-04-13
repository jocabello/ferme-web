from django.shortcuts import render
from django.http import HttpResponse


def catalogo(request):
    return render(request, 'productos/catalogo.html')


def detalle(request):
    return ('detalle')
