from django.shortcuts import render
from rest_framework import generics, permissions, status
from .serializers import CreateServiceSerializer, UpdateServiceSerializer
from .models import Service
from rest_framework.response import Response
from django_filters import rest_framework as filters
from .filters import ServiceFilter


# Create your views here.
class CreateServiceView(generics.CreateAPIView):
    serializer_class = CreateServiceSerializer
    permission_classes = [permissions.IsAuthenticated]


class UpdateServiceView(generics.UpdateAPIView):
    serializer_class = UpdateServiceSerializer
    queryset = Service.objects.filter(is_active= True)
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'pk'

class DeleteServiceView(generics.GenericAPIView):
    queryset = Service.objects.filter(is_active= True)
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'pk'
    serializer_class = CreateServiceSerializer

    def post(self, request, *args, **kwargs):
        """
        Change the activation status of a Service object and return the serialized response.
        """
        instance = self.get_object()
        new_value = instance.is_active
        instance.is_active = not new_value
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class ListServiceView(generics.ListAPIView):
    queryset = Service.objects.filter(is_active= True)
    serializer_class = CreateServiceSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = ServiceFilter
