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

    # Testing save method
    def test_save_method(self):
        self.nairobi.save_location()
        # editors = Editor.objects.all()
        # self.assertTrue(len(editors) > 0)



class CategoryTestClass(TestCase):
    #setup method
    def setUp(self):
        self.food = Category()

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.food , Category))
