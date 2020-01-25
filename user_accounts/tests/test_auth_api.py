from rest_framework.test import APITestCase, APIClient
from rest_framework import status

client = APIClient()


class AuthAPITestCase(APITestCase):
    def test_get_blogauthorsagain_success(self):
        response = client.get(
            '/api/authors/blog-authors/', allow_redirects=False)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
