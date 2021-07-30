from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.forms import ModelForm

from datetime import timedelta

from .models import Book, Author, Student


class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = '__all__'

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

class BookListView(generic.ListView):
    template_name = 'library/books.html'
    model = Book

class AuthorListView(generic.ListView):
    template_name = 'library/authors.html'
    model = Author

class BookDetailView(generic.DetailView):
    template_name = 'library/book_details.html'
    model = Book

class AuthorDetailView(generic.DetailView):
    template_name = 'library/author_details.html'
    model = Author

@login_required
def author_edit(request, pk):
    if request.method == "POST":
        author = Author.objects.get(pk=pk)
        author.delete()
    return HttpResponseRedirect(reverse('library.authors'))


@login_required
def book_edit(request, pk):
    if request.method == "POST":
        book = Book.objects.get(pk=pk)
        book.delete()
    return HttpResponseRedirect(reverse('library.books'))

@login_required
def author_delete(request, pk):
    if request.method == "POST":
        author = Author.objects.get(pk=pk)
        author.delete()
    return HttpResponseRedirect(reverse('library.authors'))


@login_required
def book_delete(request, pk):
    if request.method == "POST":
        book = Book.objects.get(pk=pk)
        book.delete()
    return HttpResponseRedirect(reverse('library.books'))

num_books = 0
num_authors = 0
num_students = 0
last_update = None

def index(request):
    if (request.user.is_authenticated or
      last_update is None or
      timezone.now()-last_update > timedelta(seconds=10)):

        num_books = Book.objects.all().count()
        num_authors = Author.objects.all().count()
        num_students = Student.objects.all().count()

    context = {
        'num_books': num_books,
        'num_authors': num_authors,
        'num_students': num_students,
    }

    return render(request, 'library/index.html', context)
