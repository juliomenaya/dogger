from utils.mixins.DetailsMixin import DetailsMixin

from .models import Schedules
from .serializers import ScheduleSerializer


class SchedulesDetailsView(DetailsMixin):
    model = Schedules
    serializer = ScheduleSerializer
