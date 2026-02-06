from rest_framework import serializers
from .models import Busapp

class BusappSerializer(serializers.ModelSerializer):
    class Meta:
        model = Busapp
        fields = '__all__'