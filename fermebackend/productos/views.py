from django.shortcuts import render
from django.http import HttpResponse


def catalogo(request):
    return HttpResponse('catálogo')


def detalle(request):
    return HttpResponse('detalle producto')
