from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth import get_user_model

class CreateCustomUserViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user_data = {
            'username': 'test_user',
            'email': 'test@example.com',
            'password': 'testpassword',
            # Add other fields if needed
        }

    def test_create_custom_user(self):
        response = self.client.post('/api/user/create/', self.user_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        # Check if the user was created in the database
        user_exists = get_user_model().objects.filter(username=self.user_data['username']).exists()
        self.assertTrue(user_exists)
        
        # Optionally, you can check if the response data matches expected serializer output
        self.assertEqual(response.data['username'], self.user_data['username'])
        self.assertEqual(response.data['email'], self.user_data['email'])


class RetriveUpdateAndDeleteCustomUserViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            username='test_user',
            email='test@example.com',
            password='testpassword'
        )
        self.client.force_authenticate(user=self.user)

    def test_retrieve_custom_user(self):
        response = self.client.get(f'/api/user/{self.user.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], self.user.username)
        self.assertEqual(response.data['email'], self.user.email)

    def test_update_custom_user(self):
        new_email = 'new_email@example.com'
        response = self.client.put(f'/api/user/{self.user.id}/', {'email': new_email})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.user.refresh_from_db()
        self.assertEqual(self.user.email, new_email)

    def test_partial_update_custom_user(self):
        new_email = 'new_email@example.com'
        response = self.client.patch(f'/api/user/{self.user.id}/', {'email': new_email})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.user.refresh_from_db()
        self.assertEqual(self.user.email, new_email)

    def test_delete_custom_user(self):
        response = self.client.delete(f'/api/user/{self.user.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(get_user_model().objects.filter(id=self.user.id).exists())



class UpdateUserPasswordViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            username='test_user',
            email='test@example.com',
            password='testpassword'
        )
        self.client.force_authenticate(user=self.user)
        self.new_password_data = {
            'new_password': 'new_testpassword'
        }

    def test_update_user_password_with_put(self):
        response = self.client.put('/api/user/password/update/', self.new_password_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.user.refresh_from_db()
        self.assertTrue(self.user.check_password(self.new_password_data['new_password']))

    def test_update_user_password_with_patch(self):
        # Attempting to update password with PATCH should return method not allowed (405)
        response = self.client.patch('/api/user/password/update/', self.new_password_data)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
