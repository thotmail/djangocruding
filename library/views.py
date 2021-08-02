from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.utils import timezone
from django.http import HttpResponseRedirect, HttpResponseBadRequest
from django.urls import reverse

from datetime import timedelta

from .models import Book, Author, Student
from .forms import *

class BookListView(generic.ListView):
    template_name = 'library/books.html'
    model = Book

class AuthorListView(generic.ListView):
    template_name = 'library/authors.html'
    model = Author

class StudentListView(generic.ListView, LoginRequiredMixin):
    template_name = 'library/students.html'
    model = Student

class BookDetailView(generic.DetailView):
    template_name = 'library/book_details.html'
    model = Book

class AuthorDetailView(generic.DetailView):
    template_name = 'library/author_details.html'
    model = Author

class StudentDetailView(generic.DetailView, LoginRequiredMixin):
    template_name = 'library/student_details.html'
    model = Student


def obj_add_edit(request, pk, obj, form_obj, obj_name, target):
    '''helper function to avoid repeated code'''
    if request.method == "POST":
        if pk is not None:
            obj_instance = get_object_or_404(obj, pk=pk)
            form = form_obj(request.POST, instance=obj_instance)
            rev = reverse(target, args=(pk,))
        else:
            form = form_obj(request.POST)
            rev = reverse(target)
        if(form.is_valid()):
            form.save()
            return HttpResponseRedirect(rev)
        else:
            return HttpResponseBadRequest("Data is invalid")
    else:
        context = {}
        if pk is not None:
            obj_instance = get_object_or_404(obj, pk=pk)
            context['form'] = form_obj(instance=obj_instance)
            context['submit_text'] = "Save"
            context['edit_title'] = "Edit "
            context['post_target'] = reverse(target, args=(pk,))
        else:
            context['form'] = form_obj()
            context['submit_text'] = "Create"
            context['edit_title'] = "Create "
            context['post_target'] = reverse(target)
        context['edit_title'] += obj_name
        return render(request, "library/addedit.html", context)
    
@login_required
def author_edit(request, pk=None):
    return obj_add_edit(request, pk, Author, AuthorForm, "Author", "library:author_edit")

@login_required
def book_edit(request, pk=None):
    return obj_add_edit(request, pk, Book, BookForm, "Book", "library:book_edit")

@login_required
def student_edit(request, pk=None):
    return obj_add_edit(request, pk, Student, StudentForm, "Student", "library:student_edit")

@login_required
def author_add(request):
    return obj_add_edit(request, None, Author, AuthorForm, "Author", "library:author_add")

@login_required
def book_add(request):
    return obj_add_edit(request, None, Book, BookForm, "Book", "library:book_add")

@login_required
def student_add(request):
    return obj_add_edit(request, None, Student, StudentForm, "Student", "library:student_add")
    

def obj_delete(request, pk, obj, target):
    if request.method == "POST":
        obj_instance = obj.objects.get(pk=pk)
        obj_instance.delete()
    return HttpResponseRedirect(reverse(target))

@login_required
def author_delete(request, pk):
    return obj_delete(request, pk, Author, 'library:authors')

@login_required
def book_delete(request, pk):
    return obj_delete(request, pk, Book, 'library:books')

@login_required
def student_delete(request, pk):
    return obj_delete(request, pk, Student, 'library:students')

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
