from django.test import TestCase
from rest_framework.test import APITestCase
from todo.factories import ReadFactory
from todo.models import Read


class ReadTest(APITestCase):

    def test_get(self):
        self.assertTrue(True)
