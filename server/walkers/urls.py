from django.urls import path
from rest_framework.routers import SimpleRouter
from rest_framework.urlpatterns import format_suffix_patterns

from .views import WalkersViewSet

router = SimpleRouter()

router.register('', WalkersViewSet)

urlpatterns = format_suffix_patterns(router.urls)
