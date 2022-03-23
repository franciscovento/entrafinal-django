from unicodedata import name
from django.db import models
from django.forms import CharField

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def getName(self):
        return self.name

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


class BookItem(Book):
    BOOK_FORMAT = (
        ("hardcover","Hardcover"),
        ("paperback", "Paperback"),
        ("audiobook", "Audiobook"),
        ("ebook", "Ebook"),
        ("newspaper", "Newspaper"),
        ("magazine", "Magazine"),
        ("journal", "Journal"),
        )
    
    BOOK_STATUS = (
        ("available", "Available"),
        ("reserved", "Reserved"),
        ("loaned", "Loaned"),
        ("lost", "Lost")
    )
    
    barcode = models.CharField(max_length=20)
    is_referenc_only = models.BooleanField(default=False)
    borrowed = models.DateField()
    due_date = models.DateField()
    price = models.FloatField()
    format = models.CharField(max_length=15, choices=BOOK_FORMAT)
    status = models.CharField(max_length=15, choices=BOOK_STATUS)
    date_of_purchase = models.DateField()
    
    def checkout(self):
        pass
    
class Account(models.Model):
    ACCOUNT_STATUS = (
        ("active", "Active"),
        ("closed", "Closed"),
        ("cancelled", "Cancelled"),
        ("blacklisted", "Blacklisted"),
        ("none", "None")
    )
    
    id = models.CharField(max_length=10, primary_key=True)
    password = models.CharField(max_length=16)
    status = models.CharField(max_length=15, choices=ACCOUNT_STATUS)
    
    def resetPassword(self):
        pass

class Librarian(Account):
    def addBookItem():
        pass
    
    def blockMember(self):
        pass
    
    def unblockMember(self):
        pass