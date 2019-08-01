from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Venta


class VentaSerializer(serializers.ModelSerializer):
    class Meta:
        model= Venta
        fields = ['id','idUsuario', 'compraJson', 'precio']