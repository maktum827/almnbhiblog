from dataclasses import field
from os import read
from django.contrib import admin

from .models import Admission , Banner, Course

# Register your models here.
admin.site.register((Admission,Banner,Course))