from django.db import models

"""
Create a model Book in the database
with 3 attributs : 
    title - title of book
    description - description of book
    author - author of book
"""


class Book(models.Model):
    title = models.CharField(max_length=70, blank=False, default="")
    description = models.CharField(max_length=200, blank=False, default="")
    author = models.CharField(max_length=50, blank=False, default="")


# Create your models here.
