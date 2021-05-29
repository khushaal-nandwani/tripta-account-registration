from django.urls import path
from .views import TFormAPIView, TFormUserDetailView, TFormCreate

urlpatterns = [
    path('users/', TFormAPIView.as_view()),
    path('users/<int:pk>/', TFormUserDetailView.as_view()),
    path('users/create/', TFormCreate.as_view()),
]
