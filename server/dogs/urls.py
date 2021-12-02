from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import DogsDetailsView

urlpatterns = [
    path('<int:pk>/', DogsDetailsView.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
