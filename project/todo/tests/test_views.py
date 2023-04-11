from django.test import TestCase
from rest_framework.test import APITestCase
from todo.factories import ReadFactory
from todo.models import Read

class StatusTest(APITestCase): 
    def test_status(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        result = response.json()
        
        self.assertEqual(result['status'], 'ok')
        self.assertEqual(result['name'], 'todo')

    def test_ping(self):
        response = self.client.get('/ping')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b'pong')


class ReadViewSetTest(APITestCase):

    def test_get_all_read(self):
        self.assertTrue(True)

