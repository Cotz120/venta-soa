from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import VentaSerializer
from .models import Venta


class VentaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Venta.objects.all()
    serializer_class = VentaSerializer