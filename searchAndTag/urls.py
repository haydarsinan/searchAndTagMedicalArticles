from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('list/', views.index),
    # path('list/', views.list_todo_items),
    # path('authors/', views.list_authors),
    # path('insert_todo/', views.insert_todo_item, name='insert_todo_item'),
    # path('delete_todo/<int:todo_id>/', views.delete_todo_items, name='delete_todo_item'),
    # path('search_authors/', views.search_authors, name='search-authors'),
]