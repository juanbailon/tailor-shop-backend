from rest_framework import serializers
from .models import RawMaterial


class RawMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = RawMaterial
        fields = '__all__'
        extra_kwargs = {
            "user_register": {"required": True},
            "name": {"required": True},
            "material_type": {"required": True},
            "remaining_amount": {"required": True},
            "unit_price": {"required": True},
            "unit_of_measure": {"required": True}
        }
    
    def create(self, validated_data):
        rawMaterial = RawMaterial(**validated_data)
        rawMaterial.save()
        return rawMaterial


class UpdateRawMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = RawMaterial
        fields = '__all__'