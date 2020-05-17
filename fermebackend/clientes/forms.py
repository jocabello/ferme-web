from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import login, authenticate
from django import forms

from clientes.models import Cliente

class RegistroForm(UserCreationForm):
    email = forms.EmailField(max_length=60, help_text='Requeridox')
   # p_natural_rut = forms.CharField(max_length=15, required=True)

    class Meta:
        model = Cliente
        fields = (
            "email",
            "p_natural_rut",
            "password1",
            "password2",
            )

class EditarCuentaForm(UserChangeForm):

    class Meta:
        model = Cliente
        fields = ('p_natural_rut', 'password')