from django.db import models

# Create your models here.

class BookList(models.Model):
    book_name = models.CharField(max_length=30)
    author = models.CharField(max_length = 15)
    description = models.CharField(max_length = 100)