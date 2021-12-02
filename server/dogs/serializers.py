from rest_framework import serializers

from .models import Dogs


class DogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dogs
        fields = '__all__'
        depth = 1
