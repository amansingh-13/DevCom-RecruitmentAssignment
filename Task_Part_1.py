from uuid import uuid4
from django.db import models

class User(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=50)
    roll_no = models.IntegerField(unique=True)
    hostel = models.CharField(max_length=20)
    phone_no = models.BigIntegerField(unique=True)
    
    def delete_book
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Name of User"
        verbose_name_plural = "Name of Users"
    
class Book(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    isbn_id = models.BigIntegerField(unique=True)
    author = models.CharField(max_length=50)
    lender=models.ForeignKey(
        User, on_delete=models.CASCADE, default=uuid4, related_name='books')
    
    def __str__(self):
        return self.name
    #add function to delete
    class Meta:
        verbose_name = "Book Title"
        verbose_name_plural = "Book Titles"
