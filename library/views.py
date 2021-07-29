from django.shortcuts import render

from .models import Book, Author, Student

from django.views import generic


class BookListView(generic.ListView):
    template_name = 'library/books.html'
    model = Book

class AuthorListView(generic.ListView):
    template_name = 'library/authors.html'
    model = Author


def indexView(request):
    num_books = Book.objects.all().count()
    num_authors = Author.objects.all().count()
    num_students = Student.objects.all().count()

    context = {
        'num_books': num_books,
        'num_authors': num_authors,
        'num_students': num_students,
    }

    return render(request, 'library/index.html', context)
