import json

from django.contrib.auth.models import User
from rest_framework import serializers


class SignUpSerializer(serializers.Serializer):
    email = serializers.EmailField()
    name = serializers.CharField()
    last_name = serializers.CharField()
    phone = serializers.CharField(max_length=10)
    password = serializers.CharField()


def register_user(model, request_payload):
    data = json.loads(request_payload)
    istance_serialized = SignUpSerializer(data=data)

    if istance_serialized.is_valid():
        user = User(
            password=data['password'],
            email=data['email'],
            username=f"{data['name']}.{data['last_name']}"
        )
        user.save()
        model_instance = model(
            name=data['name'],
            last_name=data['last_name'],
            phone=data['phone'],
            user=user
        )
        model_instance.save()
        return model_instance, None
    return None, istance_serialized.errors
