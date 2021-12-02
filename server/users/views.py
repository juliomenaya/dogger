import json

from django.contrib.auth.models import User as Auth
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from utils.mixins.DetailsMixin import DetailsMixin

from .models import Users
from .serializers import UserSerializer, UserSignUpSerializer


class UsersViewSet(ModelViewSet):
    queryset = Users.objects.all()

    @action(detail=False, methods=['post'])
    def signup(self, request):
        data = json.loads(request.body)
        serializer = UserSignUpSerializer(data=data)
        
        if serializer.is_valid():
            auth_user = Auth(
                password=data['password'],
                email=data['email'],
                username=f"{data['name']}.{data['lastname']}"
            )
            auth_user.save()
            user = Users(
                name=data['name'],
                last_name=data['lastname'],
                phone=data['phone'],
                user=auth_user
            )
            user.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class UsersDetailsView(DetailsMixin):
    """
    Retrieve, update or delete a user instance.
    """

    model = Users
    serializer = UserSerializer

    def delete(self, pk):
        account = Auth.objects.filter(pk)
        account.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
