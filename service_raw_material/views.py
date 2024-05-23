from django.shortcuts import render
from rest_framework import generics, permissions
from service_raw_material.models import ServiceRawMaterial
from .serializers import ServiceRawMaterialSerializer


class RegisterServiceRawMaterialView(generics.CreateAPIView):
    serializer_class = ServiceRawMaterialSerializer
    permission_classes = [permissions.IsAuthenticated]


class ListServiceRawMaterialView(generics.ListAPIView):
    serializer_class = ServiceRawMaterial
    permission_classes = [permissions.IsAuthenticated]