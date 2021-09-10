from django.db.models import fields
from rest_framework import serializers
from rest_framework.relations import ManyRelatedField
from .models import *
 
class ComunaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comuna
        fields = ['id_comuna', 'nombre_comuna']

class RegionSerializer(serializers.ModelSerializer):
    region = ComunaSerializer(many=True, read_only=True)
    class Meta:
        model = Region
        fields = ('id_region', 'nombre_region', 'region')
