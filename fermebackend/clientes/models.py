from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

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
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            p_natural_rut=p_natural_rut
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self.db)
        return user
    

class Cliente(AbstractBaseUser):
    email = models.EmailField(verbose_name="email", max_length=35, unique=True)
    date_joined = models.DateTimeField(verbose_name='fecha creacion', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='ultimo login', auto_now=True)
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

    p_natural_rut = models.CharField(max_length=50)
    p_natural_nombre = models.CharField(max_length=50)
    p_natural_apellido = models.CharField(max_length=50)

    empresa_rut = models.CharField(max_length=50)
    empresa_nombre = models.CharField(max_length=50)
    empresa_rol = models.CharField(max_length=50)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['p_natural_rut']

    
    objects = ManejadorDeClientes()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

