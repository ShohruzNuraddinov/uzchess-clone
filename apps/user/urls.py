from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from apps.user.views import UserSendVerificationCodeView, UserCodeVerifyView, UserSetPasswordView

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]


urlpatterns += [
    path('sendcode/', UserSendVerificationCodeView.as_view()),
    path('verifycode/', UserCodeVerifyView.as_view()),
    path('setpassword/', UserSetPasswordView.as_view())
]
