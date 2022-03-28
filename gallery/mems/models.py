from email.mime import image
from django.db import models

# Create your models here.


class Location(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
    
    def save_location(self):
        self.save()

    def delete_location(self):
        self.save()


class Category(models.Model):
    name = models.CharField(max_length=30)

    def save_category(self):
        self.save()
    
    # def update_category():
    #     self.update()

    def delete_category(self):
        self.save()

    def __str__(self):
        return self.name 

class Image(models.Model):
    image = models.ImageField(upload_to = 'images/', default='')
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=120)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def highlights(cls):
        highlights= cls.objects.order_by('category')
        return highlights
        
    @classmethod
    def get_image_by_id(cls,id):
        image_per_id=cls.objects.filter(id = id).all()
        return image_per_id

    @classmethod
    def search_image(cls,search_term):
        image =cls.objects.filter(category__name__icontains=search_term)
        return image
    
    @classmethod
    def filter_by_location(cls,location):
        image_per_location =cls.objects.filter(location__name__icontains= location)
        print(image_per_location)
        return image_per_location
   

 
       
