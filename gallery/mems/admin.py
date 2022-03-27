from django.contrib import admin
from .models import Category,Location,Image

class ImageAdmmin(admin.ModelAdmin):
    fiter_horizontal = ('category')
# Register your models here.
admin.site.register(Image,ImageAdmmin)
admin.site.register(Location)
admin.site.register(Category)

