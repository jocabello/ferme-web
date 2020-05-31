from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import login, authenticate
from django import forms

from clientes.models import Cliente

TIPO_CLIENTE = [
    ('pnatural', 'Persona natual'),
    ('empresa', 'Empresa'),
]


class RegistroForm(UserCreationForm):
    email = forms.EmailField(max_length=60, help_text='Requeridox')

    tipo_cliente = forms.ChoiceField(label='Seleccionar tipo de cuenta:',
                                     choices=TIPO_CLIENTE,
                                     widget=forms.RadioSelect)

    # p_natural_rut = forms.CharField(max_length=15, required=True)

    class Meta:
        model = Cliente
        fields = (
            "email",
            "tipo_cliente",
            "p_natural_nombre",
            "p_natural_rut",
            "password1",
            "password2",
        )


class EditarCuentaForm(UserChangeForm):
    class Meta:
        model = Cliente
        fields = ('p_natural_rut', 'p_natural_nombre', 'password')