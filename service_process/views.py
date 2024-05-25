from django.shortcuts import render
from rest_framework import generics, permissions
from .serializers import ServiceProcessSerializer, ServiceProcessInfoSerializer
from .models import ServiceProcess


class RegisterServiceProcess(generics.CreateAPIView):
    serializer_class = ServiceProcessSerializer
    permission_classes = [permissions.IsAuthenticated]


class ListServiceProcessView(generics.ListAPIView):
    queryset = ServiceProcess.objects.all()
    serializer_class = ServiceProcessInfoSerializer
    permission_classes = [permissions.IsAuthenticated]