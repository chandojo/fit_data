import unittest

from rest_framework.test import APITestCase, RequestsClient
from rest_framework import status


client = RequestsClient()


class AuthAPITestCase(APITestCase):
    def test_get_blogauthors_success(self):
        response = client.get('http://testserver/api/authors/blog-authors')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
