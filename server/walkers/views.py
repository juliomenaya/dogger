from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from utils.account import register_user
from utils.mixins.DetailsMixin import DetailsMixin

from .models import Schedules, Walkers
from .serializers import ScheduleSerializer


class WalkersViewSet(ModelViewSet):
    queryset = Walkers.objects.all()

    @action(detail=False, methods=['post'])
    def signup(self, request):
        user, errors = register_user(Walkers, request.body)
        
        if user:
            return Response(status=status.HTTP_201_CREATED)
        return Response(errors, status=status.HTTP_400_BAD_REQUEST)


class SchedulesDetailsView(DetailsMixin):
    model = Schedules
    serializer = ScheduleSerializer
