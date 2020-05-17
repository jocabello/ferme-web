from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from clientes.models import Cliente

class AdministradorClientes(UserAdmin):
    list_display = ('email', 'p_natural_rut', 'tipo_cliente', 'date_joined', 'last_login', 'is_active', 'is_staff')
    search_fields = ('email', 'p_natural_rut',)
    readonly_fields = ('date_joined', 'last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

    ordering = ('email',)


admin.site.register(Cliente, AdministradorClientes)