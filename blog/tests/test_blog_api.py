from rest_framework.test import APITestCase, APIClient
from rest_framework import status


client = APIClient()


class BlogAPITestCase(APITestCase):
    def test_get_blog_success(self):
        response = client.get(
            '/api/blog/', allow_redirects=False)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_blogentries_success(self):
        response = client.get(
            '/api/blog/blogentries/', allow_redirects=False)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
