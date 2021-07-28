from django.db import models

class Student:
    name = models.CharField(max_length=200)
