import unittest
from rest_framework.test import APITestCase
from rest_framework import status


from .views import *


class BlogEntryAPITestCase(APITestCase):
    def test_get_states(self):
        url = '/api/blog/blogentries/'
        data = {}
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
