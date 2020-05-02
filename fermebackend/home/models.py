# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Cargo(models.Model):
    id_cargo = models.IntegerField(primary_key=True)
    descripcion_cargo = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'cargo'


class Carro(models.Model):
    id_carro = models.IntegerField(primary_key=True)
    total = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'carro'


class Ciudad(models.Model):
    id_ciudad = models.IntegerField(primary_key=True)
    descripcion_ciudad = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'ciudad'


class Cliente(models.Model):
    id_cliente = models.IntegerField(primary_key=True)
    user_cliente = models.CharField(max_length=50)
    pass_cliente = models.CharField(max_length=50)
    empresa_rut_empresa = models.ForeignKey(
        'Empresa', models.DO_NOTHING, db_column='empresa_rut_empresa', blank=True, null=True)
    persona_natural_rut_natural = models.ForeignKey(
        'PersonaNatural', models.DO_NOTHING, db_column='persona_natural_rut_natural', blank=True, null=True)
    direccion_calle = models.CharField(max_length=50, blank=True, null=True)
    direccion_numero = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=35, blank=True, null=True)
    telefono = models.IntegerField(blank=True, null=True)
    comuna_id_ciudad = models.IntegerField(blank=True, null=True)
    carro_id_carro = models.ForeignKey(
        Carro, models.DO_NOTHING, db_column='carro_id_carro')
    comuna_id_comuna = models.ForeignKey(
        'Comuna', models.DO_NOTHING, db_column='comuna_id_comuna', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cliente'


class Comuna(models.Model):
    id_comuna = models.IntegerField(primary_key=True)
    descripcion_comuna = models.CharField(max_length=50)
    ciudad_id_ciudad = models.ForeignKey(
        Ciudad, models.DO_NOTHING, db_column='ciudad_id_ciudad')

    class Meta:
        managed = False
        db_table = 'comuna'


class DetalleCarro(models.Model):
    id_detalle_carro = models.IntegerField(primary_key=True)
    cantidad = models.IntegerField()
    producto_id_producto = models.ForeignKey(
        'Producto', models.DO_NOTHING, db_column='producto_id_producto')
    carro_id_carro = models.ForeignKey(
        Carro, models.DO_NOTHING, db_column='carro_id_carro')

    class Meta:
        managed = False
        db_table = 'detalle_carro'


class DetalleOrdenDeCompra(models.Model):
    id_detalle = models.IntegerField(primary_key=True)
    cantidad = models.IntegerField()
    fk_producto = models.ForeignKey(
        'Producto', models.DO_NOTHING, db_column='fk_producto')
    fk_orden = models.ForeignKey(
        'OrdenDeCompra', models.DO_NOTHING, db_column='fk_orden')
    precio_compra = models.IntegerField()
    fk_id_proveedor = models.ForeignKey(
        'OrdenDeCompra', models.DO_NOTHING, db_column='fk_id_proveedor', related_name='fk_det_a_prov')

    class Meta:
        managed = False
        db_table = 'detalle_orden_de_compra'


class DetalleVenta(models.Model):
    id_detalle_venta = models.IntegerField(primary_key=True)
    cantidad = models.IntegerField()
    venta_id_venta = models.ForeignKey(
        'Venta', models.DO_NOTHING, db_column='venta_id_venta')
    venta_id_tipo_venta = models.BooleanField()
    producto_id_producto = models.ForeignKey(
        'Producto', models.DO_NOTHING, db_column='producto_id_producto')

    class Meta:
        managed = False
        db_table = 'detalle_venta'


class Empresa(models.Model):
    rut_empresa = models.IntegerField(primary_key=True)
    dv_empresa = models.CharField(max_length=2)
    nombre_empresa = models.CharField(max_length=50)
    rol_empresa = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'empresa'


class FamilyProduct(models.Model):
    id_family = models.IntegerField(primary_key=True)
    desc_family = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'family_product'


class Funcionario(models.Model):
    rut_funcionario = models.IntegerField(primary_key=True)
    dv_funcionario = models.CharField(max_length=2)
    nombre_funcionario = models.CharField(max_length=50)
    apellido_funcionario = models.CharField(max_length=50)
    user_funcionario = models.CharField(max_length=50)
    pass_funcionario = models.CharField(max_length=50)
    cargo_id_cargo = models.ForeignKey(
        Cargo, models.DO_NOTHING, db_column='cargo_id_cargo')

    class Meta:
        managed = False
        db_table = 'funcionario'


class Imagen(models.Model):
    producto_id_producto = models.OneToOneField(
        'Producto', models.DO_NOTHING, db_column='producto_id_producto', primary_key=True)
    direccion_imagen = models.CharField(max_length=500)

    class Meta:
        managed = False
        db_table = 'imagen'


class OrdenDeCompra(models.Model):
    id_orden = models.IntegerField(primary_key=True)
    fecha = models.DateField()
    total = models.IntegerField()
    es_nula = models.CharField(max_length=1)
    proveedor_id_proveedor = models.ForeignKey(
        'Proveedor', models.DO_NOTHING, db_column='proveedor_id_proveedor')
    funcionario_rut_funcionario = models.ForeignKey(
        Funcionario, models.DO_NOTHING, db_column='funcionario_rut_funcionario')

    class Meta:
        managed = False
        db_table = 'orden_de_compra'
        unique_together = (('id_orden', 'proveedor_id_proveedor'),)


class PersonaNatural(models.Model):
    rut_natural = models.IntegerField(primary_key=True)
    dv_natural = models.CharField(max_length=2)
    nombre_natural = models.CharField(max_length=50)
    apellido_natural = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'persona_natural'


class Producto(models.Model):
    id_producto = models.BigIntegerField(primary_key=True)
    descripcion = models.CharField(max_length=100)
    precio = models.IntegerField()
    stock = models.IntegerField()
    stock_critico = models.IntegerField()
    fk_id_familia = models.IntegerField()
    fk_id_proveedor = models.ForeignKey(
        'Proveedor', models.DO_NOTHING, db_column='fk_id_proveedor')
    fk_id_product = models.ForeignKey(
        'TipoProduct', models.DO_NOTHING, db_column='fk_id_product')

    class Meta:
        db_table = 'producto'


class Proveedor(models.Model):
    id_proveedor = models.IntegerField(primary_key=True)
    nombre_proveedor = models.CharField(max_length=25)
    fono = models.BigIntegerField()
    rubro = models.CharField(max_length=50)
    user_proveedor = models.CharField(max_length=50)
    pass_proveedor = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'proveedor'


class TipoProduct(models.Model):
    id_product = models.IntegerField(primary_key=True)
    desc_product = models.CharField(max_length=40)
    family_product_id_family = models.ForeignKey(
        FamilyProduct, models.DO_NOTHING, db_column='family_product_id_family')

    class Meta:
        managed = False
        db_table = 'tipo_product'


class TipoVenta(models.Model):
    id_tipo_venta = models.BooleanField(primary_key=True)
    descripcion_tipo_vena = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'tipo_venta'


class Venta(models.Model):
    id_venta = models.IntegerField(primary_key=True)
    fecha_venta = models.DateField()
    total = models.IntegerField()
    es_nula = models.CharField(max_length=1)
    tipo_venta_id_tipo_venta = models.ForeignKey(
        TipoVenta, models.DO_NOTHING, db_column='tipo_venta_id_tipo_venta')
    cliente_id_cliente = models.ForeignKey(
        Cliente, models.DO_NOTHING, db_column='cliente_id_cliente', blank=True, null=True)
    funcionario_rut_funcionario = models.ForeignKey(
        Funcionario, models.DO_NOTHING, db_column='funcionario_rut_funcionario')

    class Meta:
        managed = False
        db_table = 'venta'
