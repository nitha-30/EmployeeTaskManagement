from django.urls import path
from user import views
from rest_framework_simplejwt import views as jwt_views


urlpatterns = [
    path('register/', views.RegisterView.as_view()),
    path('login/', jwt_views.TokenObtainPairView.as_view()),
    path('refresh/',jwt_views.TokenRefreshView.as_view())
]
