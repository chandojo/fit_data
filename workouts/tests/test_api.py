from django.test import TestCase

from rest_framework.test import APITestCase, APIRequestFactory, URLPatternsTestCase


# TODO: Write mock request

class APIRequestTestCase(APITestCase):
    def test_muscle_get_response(self):
        response = self.client.get('/muscles/')
        self.assertEqual(response.status_code, 200)

    def test_muscle_groups_get_response(self):
        response = self.client.get('/muscle-groups/')
        self.assertEqual(response.status_code, 200)

    def test_exercise_difficulty_get_response(self):
        response = self.client.get('/exercise-difficulty/')
        self.assertEqual(response.status_code, 200)

    def test_movement_get_response(self):
        response = self.client.get('/movement/')
        self.assertEqual(response.status_code, 200)
