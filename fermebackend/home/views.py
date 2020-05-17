from django.shortcuts import render
from django.http import HttpResponse
from clientes.models import Cliente


def home(request):
    return render(request, 'home/home.html')

def home_test(request):
    context={}
    clientes = Cliente.objects.all()
    context['clientes'] = clientes

    return render(request, 'personal/home', context)