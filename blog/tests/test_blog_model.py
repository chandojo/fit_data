import unittest
from django.test import TestCase

from ..models import BlogEntry
from . import fakes


class BlogEntryTestCase(TestCase):
    def test_entries_created(self):
        for _ in range(3):
            fakes.BlogEntryFactory()

        get_entries = BlogEntry.objects.count()
        expected = 3
        self.assertEqual(get_entries, expected)
