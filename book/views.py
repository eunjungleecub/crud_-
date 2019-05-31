from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy

from book.models import Post

class BookList(ListView):
    model = Post

class BookView(DetailView):
    model = Post

class BookCreate(CreateView):
    model = Post
    fields = ['title', 'author', 'date(auto)', 'comment']
    success_url = reverse_lazy('all_books')

class BookUpdate(UpdateView):
    model = Post
    fields = ['title', 'author', 'date(auto)', 'comment']
    success_url = reverse_lazy('all_books')

class BookDelete(DeleteView):
    model = Post
    success_url = reverse_lazy('all_books')
