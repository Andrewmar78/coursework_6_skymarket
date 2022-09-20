from django.urls import include, path
from djoser.views import UserViewSet
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# Подключение UserViewSet из Djoser.views к urls.py через использование SimpleRouter
users_router = SimpleRouter()
users_router.register('users', UserViewSet, basename='users')

urlpatterns = [
    path('', include(users_router.urls)),
    path('token/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
]
