from django.urls import path
from .views import SubscriberDetailAPI, RegisterUserAPIView, LoginAPI
urlpatterns = [
  path("login/", LoginAPI.as_view()),
  path('register/', RegisterUserAPIView.as_view()),
]