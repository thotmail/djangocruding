from django.contrib import admin

from .models import Author, Book, Student

admin.site.register(Student)

admin.site.register(Author)
admin.site.register(Book)
