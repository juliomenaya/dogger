from rest_framework import serializers
from .models import Users

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'
        depth = 1


class UserSignUpSerializer(serializers.Serializer):
    email = serializers.EmailField()
    name = serializers.CharField()
    lastname = serializers.CharField()
    phone = serializers.CharField(max_length=10)
    password = serializers.CharField()
