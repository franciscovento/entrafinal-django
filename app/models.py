from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    subject = models.CharField(max_length=100)
    publication_date = models.DateField()

class Rack(models.Model):
    books = models.ForeignKey(Book, on_delete=models.CASCADE)
