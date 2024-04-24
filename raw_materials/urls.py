from django.urls import path
from .views import CreateRawMaterialView, ListRawMaterialsView

urlpatterns = [
    path('create-raw-material/', CreateRawMaterialView.as_view(), name='create_raw_material'),
    path('list-raw-materials/', ListRawMaterialsView.as_view(), name='list_raw_materials'),
]