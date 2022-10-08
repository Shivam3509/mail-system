from django.urls import path
from .views import ListAPIView
urlpatterns = [
    path('index/', ListAPIView.as_view(), name ="index"),
    path('index/<int:pk>/', ListAPIView.as_view(), name ="index"),
]