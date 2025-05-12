from django.urls import path
from .views import UserRegistration, UserLogin


urlpatterns = [
    path('registration', UserRegistration.as_view()),
    path('login', UserLogin.as_view())
]