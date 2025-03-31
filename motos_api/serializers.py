# motos_api/serializers.py
from rest_framework import serializers
from .models import Moto

class MotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Moto
        fields = (
            'id',
            'reference',
            'trademark',
            'model',
            'price',
            'image',
            'supplier',
        )