from rest_framework import serializers
from .models import RawMaterial

class RawMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = RawMaterial
        fields = '__all__'
        extra_kwargs = {
            "user_register": {"required": True}
        }
    
    def create(self, validated_data):
        rawMaterial = RawMaterial(**validated_data)
        rawMaterial.save()
        return rawMaterial