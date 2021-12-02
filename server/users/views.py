from django.contrib.auth.models import User as Auth
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from utils.account import register_user
from utils.mixins.DetailsMixin import DetailsMixin

from .models import Users
from .serializers import UserSerializer


class UsersViewSet(ModelViewSet):
    queryset = Users.objects.all()

    @action(detail=False, methods=['post'])
    def signup(self, request):
        user, errors = register_user(Users, request.body)
        
        if user:
            return Response(status=status.HTTP_201_CREATED)
        return Response(errors, status=status.HTTP_400_BAD_REQUEST)
    


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
