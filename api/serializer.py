from rest_framework.serializers import ModelSerializer
from .models import *
from django.contrib.auth.models import User


class AgenteSerializer(ModelSerializer):
    class Meta:
        model = Agentes
        fields = '__all__'
        read_only_fields = ('id', "created", "updated",)


class ImagenPagosSerializer(ModelSerializer):
    class Meta:
        model = ImagenPagos
        fields = '__all__'


class ProveedorSerializer(ModelSerializer):
    class Meta:
        model = Proveedores
        fields = '__all__'

        read_only_fields = ('id', "created", "updated",)


class PagoSerializer(ModelSerializer):
    class Meta:
        model = Pagos
        fields = '__all__'
        read_only_fields = ('id', "created", "updated",)


class ProductoSerializer(ModelSerializer):
    class Meta:
        model = Productos
        fields = '__all__'
        read_only_fields = ('id', "created", "updated",)


class SalidaSerializer(ModelSerializer):
    class Meta:
        model = Salidas
        fields = '__all__'
        read_only_fields = ('id', 'pcosto', 'pventa',
                            'importe', "created", "updated",)


class CuentaSerializer(ModelSerializer):
    class Meta:
        model = CuentaCorriente
        fields = '__all__'
        read_only_fields = ('id', 'pcosto', 'pventa', 'importe',
                            'importe_final', "created", "updated",)


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
