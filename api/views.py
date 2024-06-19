from django.shortcuts import render
from .models import *
from rest_framework import viewsets, permissions
from .serializer import AgenteSerializer, ProveedorSerializer, PagoSerializer, CuentaSerializer, ProductoSerializer, SalidaSerializer, UserSerializer, ImagenPagosSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
# Create your views here.


class AgenteViewSet(viewsets.ModelViewSet):
    queryset = Agentes.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = AgenteSerializer
##############################


class ProveedorViewSet(viewsets.ModelViewSet):
    queryset = Proveedores.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProveedorSerializer


#############################


class PagoViewSet(viewsets.ModelViewSet):
    queryset = Pagos.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = PagoSerializer


class ImagenPagoViewSet(viewsets.ModelViewSet):
    queryset = ImagenPagos.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ImagenPagosSerializer

##############################


class CuentaViewSet(viewsets.ModelViewSet):
    queryset = CuentaCorriente.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CuentaSerializer

###################################


class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Productos.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProductoSerializer


################################


class SalidasViewSet(viewsets.ModelViewSet):
    queryset = Salidas.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = SalidaSerializer


@api_view(['POST'])
def login(request):
    user = get_object_or_404(User, username=request.data['username'])
    if not user.check_password(request.data['password']):
        return Response({"error": "Password invalido!"}, status=status.HTTP_400_BAD_REQUEST)

    token, created = Token.objects.get_or_create(user=user)
    serializer = UserSerializer(instance=user)

    return Response({"tokeb": token.key, "user": serializer.data}, status=status.HTTP_200_OK)


@api_view(['POST'])
def register(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

        user = User.objects.get(username=serializer.data['username'])
        user.set_password(serializer.data['password'])
        user.save()

        token = Token.objects.create(user=user)
        return Response({'token': token.key, "user": serializer.data}, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def profile(request):
    print("estas logeado!")
    serializer = UserSerializer(instance=request.user)
    return Response(serializer.data, status=status.HTTP_200_OK)
