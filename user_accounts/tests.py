import unittest
from django.test import TestCase

from .models import BlogAuthor
from . import fakes

class BlogAuthorTestCase(TestCase):
    def test_blogauthors_created(self):
        for _ in range(5):
            fakes.BlogAuthorFactory()

        get_blogauthors = BlogAuthor.objects.count()
        expected = 5
        self.assertEqual(get_blogauthors, expected)
