"""
api URL Configuration
"""
from django.urls import path
from .views import api_home
from rest_framework.authtoken.views import obtain_auth_token 
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)


# /api/
urlpatterns = [
    path('auth/', obtain_auth_token), # endpoint http://localhost:8000/api/auth/
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'), # endpoint http://localhost:8000/api/token/
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), # endpoint http://localhost:8000/api/token/refresh/
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'), # endpoint http://localhost:8000/api/token/verify/
    path("", api_home), # endpoint http://localhost:8000/api/
]
