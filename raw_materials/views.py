from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .serializers import RawMaterialSerializer, UpdateRawMaterialSerializer
from .models import RawMaterial


class CreateRawMaterialView(generics.CreateAPIView):
    """
    View to create a new RawMaterial object.
    """
    queryset = RawMaterial.objects.all()
    serializer_class = RawMaterialSerializer
    permission_classes = [permissions.IsAuthenticated]


class ListRawMaterialsView(generics.ListAPIView):
    """
    View to get a list of all RawMaterial objects.
    """
    queryset = RawMaterial.objects.filter(is_active= True)
    serializer_class = RawMaterialSerializer
    permission_classes = [permissions.IsAuthenticated]


class RetrieveUpdateRawMaterialView(generics.RetrieveUpdateAPIView):
    """
    View to get and update a specific RawMaterial object.
    """
    queryset = RawMaterial.objects.filter(is_active= True)
    serializer_class = UpdateRawMaterialSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_url_kwarg = 'pk'

    def get_object(self):
        """
        Get the specific RawMaterial object from the ID in the URL.
        """
        queryset = self.get_queryset()
        obj_id = self.kwargs.get(self.lookup_url_kwarg)
        obj = queryset.filter(id=obj_id).first()
        return obj


class DeleteRawMaterialView(generics.GenericAPIView):
    """
    View to change the activation status of a RawMaterial object.
    """
    queryset = RawMaterial.objects.filter(is_active= True)
    permission_classes = [permissions.IsAuthenticated]
    lookup_url_kwarg = 'pk'
    serializer_class = RawMaterialSerializer

    def post(self, request, *args, **kwargs):
        """
        Change the activation status of a RawMaterial object and return the serialized response.
        """
        instance = self.get_object()
        new_value = instance.is_active
        instance.is_active = not new_value
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
