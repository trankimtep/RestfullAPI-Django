from rest_framework import serializers
from car.models import Car

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ('name', 'color', 'brand')

class PostCarSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    color = serializers.CharField(max_length=20)
    brand = serializers.CharField(max_length=20)