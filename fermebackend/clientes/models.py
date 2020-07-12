from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, User

from home.models import Producto
# Create your models here.


class ManejadorDeClientes(BaseUserManager):
    def create_user(self, email, password=None, p_natural_rut=None, tipo=None):
        if not email:
            raise ValueError("Usuario debe tener un email")

        user = self.model(
            email=self.normalize_email(email),
            p_natural_rut=p_natural_rut,
        )

        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self, email, p_natural_rut, password):
        user = self.create_user(email=self.normalize_email(email),
                                password=password,
                                p_natural_rut=p_natural_rut)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self.db)
        return user


class Cliente(AbstractBaseUser):
    email = models.EmailField(verbose_name="email", max_length=35, unique=True)
    date_joined = models.DateTimeField(verbose_name='fecha creacion',
                                       auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='ultimo login',
                                      auto_now=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    tipo_cliente = models.CharField(max_length=50)
    direccion_calle = models.CharField(max_length=50)
    direccion_numero = models.CharField(max_length=50)
    comuna = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=50)
    #telefono = models.IntegerField(blank=True)
    #carro_id = models.IntegerField()

    p_natural_rut = models.CharField(
        "Rut", help_text='Campo requerido', max_length=50)
    p_natural_nombre = models.CharField(
        "Nombre", help_text='Campo requerido', max_length=50)
    p_natural_apellido = models.CharField(max_length=50)

    empresa_rut = models.CharField("Rut empresa", max_length=50)
    empresa_nombre = models.CharField("Nombre empresa", max_length=50)
    empresa_rol = models.CharField("Rol", max_length=50)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['p_natural_rut']

    objects = ManejadorDeClientes()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True


class Orden(models.Model):
    cliente = models.ForeignKey(Cliente,
                                on_delete=models.SET_NULL,
                                blank=True,
                                null=True)
    fecha_orden = models.DateTimeField(auto_now_add=True)
    finalizada = models.BooleanField(default=False, null=True, blank=False)
    id_transaccion = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.id)

    @property
    def get_total_carro(self):
        ordenproducto = self.ordenproducto_set.all()
        total = sum([item.get_total for item in ordenproducto])
        return total

    @property
    def get_items_carro(self):
        ordenproducto = self.ordenproducto_set.all()
        total = sum([item.cantidad for item in ordenproducto])
        return total


class OrdenProducto(models.Model):
    producto = models.ForeignKey(Producto,
                                 on_delete=models.SET_NULL,
                                 blank=True,
                                 null=True)
    orden = models.ForeignKey(Orden,
                              on_delete=models.SET_NULL,
                              blank=True,
                              null=True)
    cantidad = models.IntegerField(default=0, null=True, blank=True)
    fecha_agregado = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.producto.precio * self.cantidad
        return total


class DireccionDespacho(models.Model):
    cliente = models.ForeignKey(Cliente,
                                on_delete=models.SET_NULL,
                                blank=True,
                                null=True)
    orden = models.ForeignKey(Orden,
                              on_delete=models.SET_NULL,
                              blank=True,
                              null=True)
    calle = models.CharField(max_length=200, null=True)
    numero = models.CharField(max_length=50, null=True)
    zipcode = models.CharField(max_length=50, null=True)
    comentario = models.CharField(max_length=200, null=True)
    fecha_agregado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.calle + self.numero + self.comentario
