from email.mime import image
from django.db import models

# Create your models here.


class Location(models.Model):
    name : models.CharField(max_length=30)

    def save_location(self):
        self.save()

    def delete_location(self):
        self.save()

    def __str__(self):
        return self.name

  

class Category(models.Model):
    name : models.CharField(max_length=30)

    def save_category(self):
        self.save()

    def delete_category(self):
        self.save()

    def __str__(self):
        return self.name

class Image(models.Model):
  
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=80)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    def __str__(self):
        return
       
