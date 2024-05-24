from django.urls import path
from .views import RegisterServiceRawMaterialView

urlpatterns = [
    path('register/', RegisterServiceRawMaterialView.as_view(), name='register'),
    path('list/', ListServiceRawMaterialView.as_view(), name='list')
]