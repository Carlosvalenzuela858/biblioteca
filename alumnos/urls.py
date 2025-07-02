from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenBlacklistView
)
from .views import RegisterView

urlpatterns = [
    path('registrarse/', RegisterView.as_view(), name='registrarse'),
    path('iniciarsesion/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
]
