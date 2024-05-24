from django.urls import path
from .views import CreateProcessView, ListProcessView

urlpatterns = [
    path('register/', CreateProcessView.as_view(), name='register'),
    path('list/', ListProcessView.as_view(), name='list')
]