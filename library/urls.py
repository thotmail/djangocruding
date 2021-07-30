from django.urls import path, include

from . import views

app_name = 'library'

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('students/', views.StudentListView.as_view(), name='students'),

    path('books/<int:pk>/', views.BookDetailView.as_view(), name='book_details'),
    path('authors/<int:pk>/', views.AuthorDetailView.as_view(), name='author_details'),
    path('students/<int:pk>/', views.StudentDetailView.as_view(), name='student_details'),
    
    path('books/<int:pk>/delete/', views.book_delete, name='book_delete'),
    path('authors/<int:pk>/delete/', views.author_delete, name='author_delete'),
    path('students/<int:pk>/delete/', views.student_delete, name='student_delete'),
    
    path('books/<int:pk>/edit/', views.book_edit, name='book_edit'),
    path('authors/<int:pk>/edit/', views.author_edit, name='author_edit'),
    path('students/<int:pk>/edit/', views.student_edit, name='student_edit'),
    
    path('books/add', views.book_add, name='book_add'),
    path('authors/add', views.author_add, name='author_add'),
    path('student/add', views.student_add, name='student_add'),
    
]