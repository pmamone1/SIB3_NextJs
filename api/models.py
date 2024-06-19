from datetime import timezone
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User


######## Tablas #########
ESTADOS = {
    "Pendiente": "Pendiente",
    "Vencido": "Vencido",
    "Liquidado": "Liquidado",
}

TIPO_DOCUMENTO = {
    "FC": "FC",
    "FCE": "FCE",
    "NC": "NC",
    "NCE": "NCE",
    "ND": "ND",
}

TIPO_PAGO = (
    ('Cta_cte', 'Cta_cte'),
    ('Factura', 'Factura'),
    ('FCE', 'FCE'),
    ('Ajuste', 'Ajuste'),
)

# Create your models here.


class Agentes(models.Model):
    nombre = models.CharField(max_length=25, unique=True)
    codigo_agente = models.CharField(
        max_length=15, null=True, blank=True)
    razon_social = models.CharField(max_length=50, null=True, blank=True)
    cuit = models.CharField(max_length=50, null=True, blank=True)
    provincia = models.CharField(max_length=25, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active_user = models.ForeignKey(
        settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            # Only set added_by during the first save.
            obj.added_by = request.user

        super().save_model(request, obj, form, change)

    def __str__(self):
        return f'{self.codigo_agente} - {self.nombre}'


"""
    def save_model(self, request, obj, form, change):
        obj.active_user = request.user
        super().save_model(request, obj, form, change)
"""


class Proveedores(models.Model):
    razon_social = models.CharField(max_length=50)
    contacto = models.CharField(max_length=50, null=True, blank=True)
    cuit = models.CharField(max_length=50, null=True, blank=True)
    direccion = models.CharField(max_length=80, null=True, blank=True)
    telefono = models.CharField(max_length=50, null=True, blank=True)
    Obs = models.CharField(max_length=100, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.razon_social


class Pagos(models.Model):
    proveedor = models.ForeignKey(Proveedores, on_delete=models.CASCADE)
    agente = models.ForeignKey(Agentes, on_delete=models.CASCADE)
    fecha = models.DateField(null=False, blank=False)
    importe = models.DecimalField(max_digits=18, decimal_places=2)
    tipo_pago = models.CharField(
        max_length=30, choices=TIPO_PAGO, default="Cta_cte")
    nro_documento = models.CharField(
        max_length=40, verbose_name="Nro de Documento", default="0")
    reintegro_gasto = models.BooleanField(
        default=False, blank=True, verbose_name="Reintegro de Gasto")
    acreditado = models.BooleanField(default=False, verbose_name="Acreditado")
    fecha_acreditado = models.DateField(
        verbose_name="Fecha de Acreditado", null=True, blank=True)
    doc_acreditacion = models.CharField(
        max_length=50, verbose_name="Nro de Acreditacion", null=True, blank=True)
    imagen = models.FileField(upload_to="pagos_imagen", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Pago"
        verbose_name_plural = "Pagos"
        ordering = ["-fecha"]

    def __str__(self):
        return f'{self.fecha}-{self.proveedor}- ${self.importe}'


class ImagenPagos(models.Model):
    imagen = models.FileField(upload_to="pagos_imagen", null=True, blank=True)
    pago = models.ForeignKey(
        Pagos, on_delete=models.CASCADE, related_name='imagenes_pagos')

    class Meta:
        verbose_name = "Imagen Pago"
        verbose_name_plural = "Imagen Pagos"


class CuentaCorriente(models.Model):
    proveedor = models.ForeignKey(Proveedores, on_delete=models.CASCADE)
    agente = models.ForeignKey(Agentes, on_delete=models.CASCADE)
    fecha = models.DateField(null=False, blank=False)
    tipo_documento = models.CharField(max_length=30, choices=TIPO_DOCUMENTO)
    nro_documento = models.CharField(max_length=50, null=False, blank=False)
    alicuota = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    importe = models.DecimalField(max_digits=18, decimal_places=2)
    importe_final = models.DecimalField(
        max_digits=18, decimal_places=2, null=True, blank=True)
    fecha_devolucion = models.DateField(null=True, blank=True)
    fecha_vencimiento = models.DateField(null=False, blank=False)
    estado = models.CharField(
        max_length=30, choices=ESTADOS, default="Pendiente")
    pago = models.ForeignKey(
        Pagos, null=True, blank=True, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Productos(models.Model):
    proveedor = models.ForeignKey(Proveedores, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    Porc_costo = models.DecimalField(max_digits=18, decimal_places=2)
    Porc_venta = models.DecimalField(max_digits=18, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Salidas(models.Model):
    Proveedor = models.ForeignKey(Proveedores, on_delete=models.CASCADE)
    agente = models.ForeignKey(Agentes, on_delete=models.CASCADE)
    fecha_salida = models.DateField()
    producto = models.ForeignKey(Productos, on_delete=models.CASCADE)
    edicion = models.CharField(max_length=15)
    pvp = models.DecimalField(max_digits=18, decimal_places=2)
    ri = models.DecimalField(max_digits=18, decimal_places=2)
    p_costo = models.DecimalField(max_digits=18, decimal_places=2)
    P_venta = models.DecimalField(max_digits=18, decimal_places=2)
    alicuota = models.DecimalField(max_digits=5, decimal_places=2)
    cantidad = models.IntegerField()
    devolucion = models.IntegerField(null=True, blank=True)
    Venta = models.IntegerField(null=True, blank=True)
    importe = models.DecimalField(
        max_digits=18, decimal_places=2, null=True, blank=True)
    fecha_devolucion = models.DateField()
    fecha_pago = models.DateField()
    estado = models.CharField(max_length=20, choices=ESTADOS)
    nro_pago = models.CharField(max_length=20, null=True, blank=True)
    fecha_pago = models.DateField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
