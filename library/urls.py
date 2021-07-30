from django.urls import path, include

from . import views

app_name = 'library'

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('books/<int:pk>/', views.BookDetailView.as_view(), name='book_details'),
    path('authors/<int:pk>/', views.AuthorDetailView.as_view(), name='author_details'),
    path('books/<int:pk>/delete/', views.book_delete, name='book_delete'),
    path('authors/<int:pk>/delete/', views.author_delete, name='author_delete'),
    
]