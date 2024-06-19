from django.urls import path, re_path
from .views import AgenteViewSet, SalidasViewSet, ProductoViewSet, ProveedorViewSet, PagoViewSet, CuentaViewSet, ImagenPagoViewSet
from . import views
from rest_framework import routers

router = routers.DefaultRouter()

router.register('api/agentes', AgenteViewSet, 'agentes'),
router.register('api/pagos', PagoViewSet, 'pagos'),
router.register('api/pagos/imagen', ImagenPagoViewSet, 'Imagen_pagos'),
router.register('api/proveedores', ProveedorViewSet, 'proveedores'),
router.register('api/producto', ProductoViewSet, 'productos'),
router.register('api/salidas', SalidasViewSet, 'salidas'),
router.register('api/cuenta', CuentaViewSet, 'cuenta'),

urlpatterns = router.urls
