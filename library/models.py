from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=200)


class Author(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateField()
    publisher = models.CharField(max_length=200)
    synopsis = models.TextField(null=True, blank=True)
    authors = models.ManyToManyField(Author)
    img_url = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.title
