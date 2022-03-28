from unicodedata import category
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
    def test_save_location(self):
        self.nairobi.save_location()
        location = Location.objects.all()
        self.assertTrue(len(location) > 0)

    # Testing delete method
    def test_delete_location(self):
        self.nairobi.delete_location()
        location = Location.objects.all()
        self.assertEqual(len(location),0)



class CategoryTestClass(TestCase):
    #setup method
    def setUp(self):
        self.food = Category()

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.food , Category))

    # Testing save method
    def test_save_category(self):
        self.food.save_category()
        category = Category.objects.all()
        self.assertTrue(len(category) > 0)

    # Testing delete method
    def test_delete_category(self):
        self.food.delete_category()
        category =Category.objects.all()
        self.assertEqual(len(category),0)

class ImageTestClass(TestCase):

    def setUp(self):
        # Creating a new editor and saving it
        self.nairobi= Location(name='nairobi')
        self.nairobi.save_location()

        # Creating a new tag and saving it
        self.new_category = category(name = 'testing')
        self.new_category.save()
       
        self.new_image= Image(name = 'pizza',description = 'Nairobis favourite',location = self.nairobi , category = self.food)
        self.new_image.save()

        self.new_image.category.add(self.new_category)


    def tearDown(self):
        Category.objects.all().delete()
        Location.objects.all().delete()
        Image.objects.all().delete()