from django.contrib.auth.hashers import check_password
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from .models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):    
    
    class Meta:
        model = CustomUser
        fields = ['id',
                  'email',
                  'password',
                  'role' 
                 ]        
        extra_kwargs = {
            'id': {'read_only': True},
            'password': {'write_only': True},
             }
        
        
    def create(self, validated_data):
        password = validated_data.pop('password')
        person = CustomUser(**validated_data)
        person.set_password(password)
        person.save()
        
        return person
    


class UpdateCustomUserSerializer(serializers.ModelSerializer):
    """ 
    This serializer is for updating the user info, but only NOT critical data
    that why the password field is not included 
    """
    
    class Meta:
        model = CustomUser
        fields = ['id',
                  'email',
                 ]        
        extra_kwargs = {
            'id': {'read_only': True},
             }


class PasswordUpdateSerializer(serializers.Serializer):

    current_password = serializers.CharField(max_length=200, write_only=True)
    new_password = serializers.CharField(max_length=200, write_only=True)
    confirm_new_password = serializers.CharField(max_length=200, write_only=True)

    def validate(self, data):
        """
        Custom validation to ensure current_password matches the users DB password
        and new_password is confirmed correctly.
        """

        current_password = data.get('current_password')
        new_password = data.get('new_password')
        confirm_new_password = data.get('confirm_new_password')

        # Check if new_password and confirm_new_password match
        if new_password != confirm_new_password:
            raise serializers.ValidationError("New passwords do not match.")

        
        # Check if current_password matches the user's actual password
        user = self.context['request'].user  # Assuming the user is already authenticated
        if not check_password(current_password, user.password):
            raise serializers.ValidationError("Current password is incorrect.")
        

        try:
            validate_password(new_password, user)
        except serializers.ValidationError as e:
            raise serializers.ValidationError({'new_password': e.messages})


        return data
