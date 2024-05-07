from django.urls import path
from .views import CreateRawMaterialView, ListRawMaterialsView, RetrieveUpdateRawMaterialView, DeleteRawMaterialView

urlpatterns = [
    path('create-raw-material/', CreateRawMaterialView.as_view(), name='create_raw_material'),
    path('list-raw-materials/', ListRawMaterialsView.as_view(), name='list_raw_materials'),
    path('get-update-raw-material/<int:pk>/', RetrieveUpdateRawMaterialView.as_view(), name='retreive_update_raw_materials'),
    path('delete-raw-material/<int:pk>/', DeleteRawMaterialView.as_view(), name='delete_raw_materials')
]