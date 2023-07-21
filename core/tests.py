from django.test import TestCase
from rest_framework.test import APIClient, APITestCase
from models import Customer
from django.urls import reverse

# Create your tests here.
class SimpleTest(APITestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.path = reverse('home')
        # response = client.get('/')
        # self.assertEqual(response.status_code, 200)
        
    def test_assert_into_db(self):
        path = reverse('add')
        payload = {'name':'Kilo Rent', 'sex':'Female', 'address':'HCM'}
        response = client.post(path, payload)
        self.assertTrue(response, 200)
        
        
    # def test_true(self):
    #     self.assertEqual(1, 1)
        
    # def test_response(self):
    #     # response = self.client.get(self.path)
    #     # print(response)
    #     self.assertEqual(200, 200)