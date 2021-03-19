from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import RegisterView

urlpatterns = [
    path('', TokenObtainPairView.as_view()),
    path('/refresh', TokenRefreshView.as_view()),
    path('/register', RegisterView.as_view())
]
