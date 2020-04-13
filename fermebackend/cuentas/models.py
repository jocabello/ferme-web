from django.db import models

# Create your models here.


class ClienteNatural(models.Model):
    nombre = models.CharField(max_length=200, null=True)
    apellido = models.CharField(max_length=200, null=True)
    rut = models.CharField(max_length=200, null=True)
    dv = models.CharField(max_length=200, null=True)

