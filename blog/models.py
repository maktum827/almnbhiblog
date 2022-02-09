import re
from django.db import models
from django.template.defaultfilters import truncatechars
from django.utils.safestring import mark_safe

# Create your models here.
class Admission(models.Model):
    admit_id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 300, default="")
    address = models.CharField(max_length = 300, default="")
    mobile = models.CharField(max_length = 300, default="")
    email = models.CharField(max_length = 300, default="")
    image = models.ImageField(upload_to = "screenshots/images", default ="")

    @property
    def short_description(self):
        return truncatechars(self.description, 20)

    def admin_photo(self):
        return mark_safe('<img src="{}" width="100" />'.format(self.image.url))
    admin_photo.short_description ='Image'
    admin_photo.allow_tags = True

    def __str__(self):
        return self.name

        

class Banner(models.Model):
    name = models.CharField(max_length = 300, default="Banner Image")
    image = models.ImageField(upload_to = "images", default ="")

    def __str__(self):
        return self.name


class Course(models.Model):
    title = models.CharField(max_length = 300, default="")
    description = models.CharField(max_length = 500, default="")
    image = models.ImageField(upload_to = "courses", default ="")

    def __str__(self):
        return self.title