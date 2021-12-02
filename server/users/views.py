from django.contrib.auth.models import User as Auth
from rest_framework import status
from rest_framework.response import Response
from utils.mixins.DetailsMixin import DetailsMixin

from .models import Users
from .serializers import UserSerializer


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
