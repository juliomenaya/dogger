from django.urls import path
from rest_framework.routers import SimpleRouter
from rest_framework.urlpatterns import format_suffix_patterns

from .views import UsersDetailsView, UsersViewSet

router = SimpleRouter()

router.register('', UsersViewSet)

urlpatterns = [
    path('<int:pk>/', UsersDetailsView.as_view()),
] + router.urls

urlpatterns = format_suffix_patterns(urlpatterns)

