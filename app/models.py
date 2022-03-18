from unicodedata import name
from django.db import models
from django.forms import CharField

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    #def getName(self):
    #   return self.name

class Category(models.Model):
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.category

class Book(models.Model):
    title = models.CharField(max_length=150)
    author = models.ManyToManyField(Author)
    category = models.ManyToManyField(Category)
    subject = models.CharField(max_length=100)
    publication_date = models.DateField()

class Rack(models.Model):
    books = models.ForeignKey(Book, on_delete=models.CASCADE)
