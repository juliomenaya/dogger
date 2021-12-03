from django.contrib.auth.models import User as Auth
from django.http import Http404
from dogs.models import Dogs, DogSize
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

    def get_user(self, user_id):
        try:
            return Users.objects.get(id=user_id)
        except Users.DoesNotExist:
            raise Http404

    def get_size(self, size):
        try:
            return DogSize.objects.get(size__iexact=size)
        except DogSize.DoesNotExist:
            raise Http404
    
    def create_dog(self):
        payload = self.request.data

        for key in ['user_id', 'size', 'name', 'age']:
            if key not in payload:
                raise Http404(f'Missing {key} in payload')
        
        user = self.get_user(int(payload['user_id']))
        size = self.get_size(payload['size'])

        dog = Dogs(
            name=payload['name'],
            age=int(payload['age']),
            size=size,
            owner=user
        )
        dog.save()

        return Response(
            data=dict(
                name=dog.name,
                age=dog.age,
                size=size.size
            ),
            status=status.HTTP_201_CREATED
        )
    
    def list_dogs(self):
        user_id = self.request.query_params.get('userId')
        if not user_id:
            raise Http404('Url must contain userId param')
        
        dogs = Dogs.objects.select_related('size').filter(owner__id=user_id)
        return Response(
            data=[
                {
                    'name': dog.name,
                    'age': dog.age,
                    'size': dog.size.size
                } for dog in dogs
            ],
            status=status.HTTP_200_OK
        )

    @action(detail=False, methods=['post'])
    def signup(self, request):
        user, errors = register_user(Users, request.body)
        
        if user:
            return Response(status=status.HTTP_201_CREATED)
        return Response(errors, status=status.HTTP_400_BAD_REQUEST)
    

    @action(detail=False, methods=['post', 'get'])
    def dogs(self, request):
        if request.method == 'POST':
            return self.create_dog()

        return self.list_dogs()


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
