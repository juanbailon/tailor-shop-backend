from django.urls import path
from .views import CreateRawMaterialView

urlpatterns = [
    path('create-raw-material/', CreateRawMaterialView.as_view(), name='create_raw_material'),
]