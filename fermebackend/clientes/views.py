from django.shortcuts import render, redirect
from django.contrib.auth import logout, update_session_auth_hash

from clientes.forms import RegistroForm, EditarCuentaForm

from django.contrib.auth.forms import PasswordChangeForm


def registro(response):
    if response.method == "POST":
        form = RegistroForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = RegistroForm()

    return render(response, "clientes/registro.html", {"form": form})


from django.contrib.auth import logout


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


# def carro(request):
#     if request.user.is_authenticated:
#         cliente = request.user.cliente
