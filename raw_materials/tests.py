from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import RawMaterial
from .serializers import RawMaterialSerializer
from django.contrib.auth import get_user_model

class CreateRawMaterialViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            username='test_user',
            email='test@example.com',
            password='testpassword'
        )
        self.client.force_authenticate(user=self.user)
        self.raw_material_data = {
            'name': 'Test Raw Material',
            'quantity': 10,
            # Add other required fields for RawMaterial if any
        }

    def test_create_raw_material(self):
        response = self.client.post('/api/raw_materials/create/', self.raw_material_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        # Check if the raw material was created in the database
        raw_material_exists = RawMaterial.objects.filter(name=self.raw_material_data['name']).exists()
        self.assertTrue(raw_material_exists)
        
        # check if the response data matches expected serializer output
        serializer = RawMaterialSerializer(instance=RawMaterial.objects.get(name=self.raw_material_data['name']))
        self.assertEqual(response.data, serializer.data)