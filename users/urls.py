from django.urls import path
from users.views import (UserCreateAPIView,
                         UserProfileAPIView,
                         UserUpdateAPIView)
from users.apps import UsersConfig
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView,)


app_name = UsersConfig.name

urlpatterns = [
    path('create/', UserCreateAPIView.as_view(), name='user_create'),
    path('profile/', UserProfileAPIView.as_view(), name='profile'),
    path('update/<int:pk>/', UserUpdateAPIView.as_view(), name='profile_update'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh')
]
