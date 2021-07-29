from django.urls import path, include

from . import views

app_name = 'library'

urlpatterns = [
    path('', views.indexView, name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('authors/', views.AuthorListView.as_view(), name='authors'),

]