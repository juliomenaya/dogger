from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import SignInView


urlpatterns = [
    path('login/', SignInView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
