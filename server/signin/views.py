import json

from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User as Auth
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class SignInView(APIView):

    def post(self, request):
        payload = json.loads(request.body)
        if 'email' not in payload or 'password' not in payload:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        try:
            user = Auth.objects.get(email=payload['email'])
            if check_password(payload['password'], user.password):
                return Response(status=status.HTTP_200_OK)
            return Response('Wrong password', status=status.HTTP_401_UNAUTHORIZED)
        except Auth.DoesNotExist:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
