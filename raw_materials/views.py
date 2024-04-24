from django.shortcuts import render
from rest_framework import generics, permissions
from .serializers import RawMaterialSerializer
from .models import RawMaterial

# Create your views here.

class CreateRawMaterialView(generics.CreateAPIView):
    queryset = RawMaterial.objects.all()
    serializer_class = RawMaterialSerializer
    permission_classes = [permissions.IsAuthenticated]


class ListRawMaterialsView(generics.ListAPIView):
    queryset = RawMaterial.objects.all()
    serializer_class = RawMaterialSerializer
    permission_classes = [permissions.IsAuthenticated]