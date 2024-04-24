from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import CustomUser
from .serializers import (  
    CustomUserSerializer, 
    UpdateCustomUserSerializer,
    PasswordUpdateSerializer, 
    )

# Create your views here.

class CreateCustomUserView(generics.CreateAPIView):
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.AllowAny]


class RetriveUpdateAndDeleteCustomUserView(generics.RetrieveUpdateDestroyAPIView):
    """ 
    This view lets the users consult and update his own data, in the updates the user 
    can NOT change the password, since this is consider a critical task and therefor is
    assing to an especific endpoint.

    Also lets the user delete it self from the database
    """
    queryset = CustomUser.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return CustomUserSerializer
        elif self.request.method in ('PUT', 'PATCH'):
            return UpdateCustomUserSerializer
        else:
            return CustomUserSerializer
        

class UpdateUserPasswordView(generics.UpdateAPIView):
    """ this view updates the user password, this change can only be done through a PUT, NOT a PATCH """
    
    serializer_class =  PasswordUpdateSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = CustomUser.objects.all()

    http_method_names = ['put'] # thsi makes only the PUT available and the PATCH inavailabe

    def put(self, request, *args, **kwargs):

        serializer = self.get_serializer(data= request.data)
        serializer.is_valid(raise_exception=True)
        
        new_password = serializer.validated_data['new_password']
        user = request.user
        user.set_password(new_password)
        user.save()

        return Response({"message": "Password updated successfully"}, status=status.HTTP_200_OK)