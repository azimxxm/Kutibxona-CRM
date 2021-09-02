from rest_framework import serializers
from .models import *


class LavozimSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lavozim
        fields = '__all__'


class XodimlarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Xodimlar
        fields = '__all__'


class JanirSerializer(serializers.ModelSerializer):
    class Meta:
        model = Janir
        fields = '__all__'


class NashriyotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nashriyot
        fields = '__all__'


class Kitob_tillariSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kitob_tillari
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class KitoblarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kitoblar
        fields = '__all__'


class Berilgan_kitoblarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Berilgan_kitoblar
        fields = '__all__'
