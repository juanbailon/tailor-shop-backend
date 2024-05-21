from django.urls import path
from .views import RegisterServiceProcess

urlpatterns = [
    path('Register-service-process/', RegisterServiceProcess.as_view(), name='Register-Service-Process')
]
