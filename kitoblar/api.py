from .models import *

from rest_framework import viewsets, permissions
from .serializers import *

class LavozimViewSet(viewsets.ModelViewSet):
    queryset = Lavozim.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = LavozimSerializer


class XodimlarViewSet(viewsets.ModelViewSet):
    queryset = Xodimlar.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = XodimlarSerializer


class JanrViewSet(viewsets.ModelViewSet):
    queryset = Janir.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = JanirSerializer


class NashriyotViewSet(viewsets.ModelViewSet):
    queryset = Nashriyot.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = NashriyotSerializer


class Kitob_tillariViewSet(viewsets.ModelViewSet):
    queryset = Kitob_tillari.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = Kitob_tillariSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = StudentSerializer

class KitoblarViewSet(viewsets.ModelViewSet):
    queryset = Kitoblar.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = KitoblarSerializer

class Berilgan_kitoblarViewSet(viewsets.ModelViewSet):
    queryset = Berilgan_kitoblar.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = Berilgan_kitoblarSerializer

