from utils.mixins.DetailsMixin import DetailsMixin

from .models import Dogs
from .serializers import DogSerializer


class DogsDetailsView(DetailsMixin):
    model = Dogs
    serializer = DogSerializer
