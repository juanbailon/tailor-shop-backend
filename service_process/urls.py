from django.urls import path
from .views import RegisterServiceProcess, ListServiceProcessView

urlpatterns = [
    path('register/', RegisterServiceProcess.as_view(), name='register'),
    path('list/', ListServiceProcessView.as_view(), name='list')
]
