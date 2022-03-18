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
    publication_date = models.DateField()
    
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
    
    id = models.CharField(max_length=10)
    password = models.CharField(max_length=16)
    status = models.CharField(max_length=15, choices=ACCOUNT_STATUS)
    
    def resetPassword(self):
        pass

class Librarian(Account):
    def addBookItem():
        pass
    
    def BlockMember(self):
        pass
    
    def unblockMember(self):
        pass