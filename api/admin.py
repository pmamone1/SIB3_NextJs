from django.contrib import admin
from .models import *
from django.contrib.auth.models import User


class ProveedoresAdmin(admin.ModelAdmin):
    save_on_top = True
    model = Proveedores
    list_display_links = ['razon_social', 'id',]
    list_display = ('id', 'razon_social')
    list_per_page = 5  # No of records per page

    class Meta:
        verbose_name_plural = "Proveedores"


class AgentesAdmin(admin.ModelAdmin):
    save_on_top = True
    model = Agentes
    list_display = ['nombre', 'codigo_agente',
                    'razon_social', 'active_user', 'id',]

    class Meta:
        verbose_name_plural = "Agentes"


class ImagenPagosAdmin(admin.ModelAdmin):
    model = ImagenPagos
    list_display = ['id', 'imagen', 'pago']


class ImagenPAgosAdmin(admin.TabularInline):
    model = ImagenPagos
    extra = 0


class PagosAdmin(admin.ModelAdmin):
    save_on_top = True
    # list_display = ('agente','editorial','fecha','tipo_pago','tipo_documento','nro_documento','importe',)
    list_display = ('id', 'fecha', 'agente', 'proveedor', 'tipo_pago', 'tipo_pago', 'nro_documento',
                    'importe', 'imagen', 'acreditado', 'fecha_acreditado', 'doc_acreditacion', 'reintegro_gasto',)
    list_filter = ('acreditado', 'proveedor', 'agente', 'reintegro_gasto',)
    search_fields = ('fecha', 'importe', 'proveedor', 'agente',)
    list_editable = ('acreditado', 'fecha_acreditado', 'doc_acreditacion',
                     'imagen', 'reintegro_gasto', 'fecha_acreditado',)
    ordering = ['-fecha']
    list_per_page = 6  # No of records per page
    inlines = [
        ImagenPAgosAdmin
    ]
    extra = 0


class CuentaCorrienteAdmin(admin.ModelAdmin):
    pass


class ProductosAdmin(admin.ModelAdmin):
    pass


class SalidasAdmin(admin.ModelAdmin):
    pass


# Register your models here.
admin.site.register(Proveedores, ProveedoresAdmin)
admin.site.register(Agentes, AgentesAdmin)
admin.site.register(Productos, ProductosAdmin)
admin.site.register(CuentaCorriente, CuentaCorrienteAdmin)
admin.site.register(Salidas, SalidasAdmin)
admin.site.register(Pagos, PagosAdmin)
admin.site.register(ImagenPagos, ImagenPagosAdmin)
