from django.urls import path
from .views import RegisterServiceRawMaterialView

urlpatterns = [
    path('register-service-rawmaterial/', RegisterServiceRawMaterialView.as_view(), name='register-service-rawmaterial')
]