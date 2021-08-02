from .models import Book, Author, Student
from django.forms import ModelForm


class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = '__all__'

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'