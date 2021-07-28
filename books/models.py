from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=200)

class Book(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateField()
    publisher = models.CharField(max_length=200)
    synopsis = models.TextField()
    authors = models.ManyToManyField(Author)
