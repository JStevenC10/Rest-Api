from django.test import TestCase

from .models import Gender
# Create your tests here.

class GenderTestCase(TestCase):

    def setUp(self):
        self.gender = Gender.objects.create(name='Test gender', state=True)

    def test_gender_created(self):
        self.assertGreater(len(self.gender.name), 3)
        self.assertEqual(self.gender.state, True)
        # self.assertEquals(self.gender.name, 'holamundo')
        self.assertTrue(self.gender.state)