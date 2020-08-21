from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
import views

urlpatterns = [
    path('users/', views.Users.as_view()),
    path('users/<int:pk>/', views.UsersDetail.as_view()),
    path('dogs/', views.Dogs.as_view()),
    path('dogs/<int:pk>/', views.DogsDetail.as_view()),
    path('dog-size/', views.DogSize.as_view()),
    path('dog-size/<int:pk>/', views.DogSizeDetail.as_view()),
    path('schedule/', views.Schedules.as_view()),
    path('schedule/<int:pk>/', views.SchedulesDetail.as_view()),
    path('scheduled-walks/', views.ScheduledWalks.as_view()),
    path('scheduled-walks/<int:pk>/', views.ScheduledWalksDetails.as_view()),
    path('walkers/', views.Walkers.as_view()),
    path('walkers/<int:pk>/', views.WalkersDetails.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)