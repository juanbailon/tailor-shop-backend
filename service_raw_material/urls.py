from django.urls import path
from .views import *

utlpatterns = [
    path('register-service-rawmaterial/', RegisterServiceRawMaterialView.as_view(), name='register-service-rawmaterial')
]