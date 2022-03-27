from django.test import TestCase
from .models import Image,Location,Category

# Create your tests here.
class LocationTestClass(TestCase):
    #setup method
    def setUp(self):
        self.nairobi = Location()

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.nairobi , Location))


class CategoryTestClass(TestCase):
    #setup method
    def setUp(self):
        self.food = Category()

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.food , Category))
