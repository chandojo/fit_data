import unittest

from rest_framework.test import APITestCase, RequestsClient
from rest_framework import status


client = RequestsClient()


class BlogAPITestCase(APITestCase):
    def test_get_blog_success(self):
        response = client.get('http://testserver/api/blog/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_blogentries_success(self):
        response = client.get('http://testserver/api/blog/blogentries/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
