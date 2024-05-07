from django.urls import path
from .views import CreateServiceView, UpdateServiceView

urlpatterns = [
    path('create-service/', CreateServiceView.as_view(), name='create-service'),
    path('update-service/<int:pk>/', UpdateServiceView.as_view(), name='update-service'),
]