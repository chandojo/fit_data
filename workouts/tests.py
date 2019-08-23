from django.test import TestCase
import .models

# Create your tests here.
class WorkoutLabelTestCase(TestCase):
    def test_workout_name_label(self):
        field_label = State._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_slug_name_label(self):
        field_label = State._meta.get_field('slug').verbose_name
        self.assertEquals(field_label, 'slug')
