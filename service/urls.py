from django.urls import path
from .views import CreateServiceView, UpdateServiceView, DeleteServiceView, ListServiceView

urlpatterns = [
    path('create-service/', CreateServiceView.as_view(), name='create-service'),
    path('update-service/<int:pk>/', UpdateServiceView.as_view(), name='update-service'),
    path('delete-service/<int:pk>/', DeleteServiceView.as_view(), name='delete-service'),
    path('list-service/', ListServiceView.as_view(), name='list-service'),
]