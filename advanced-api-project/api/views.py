from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
from .models import Book

class BookListView(ListView):
    model = Book
    template_name = 'book_list.html'
    context_object_name = 'books' 

class BookDetailView(DetailView):
    model = Book
    template_name = 'book_detail.html'

class BookCreateView(CreateView):
    model = Book
    template_name = 'book_create.html'
    fields = ['title', 'author', 'description', 'published_date']

class BookUpdateView(UpdateView):
    model = Book
    template_name = 'book_update.html'
    fields = ['title', 'author', 'description', 'published_date']

class BookDeleteView(DeleteView):
    model = Book
    template_name = 'book_delete.html'
    success_url = '/'  # Redirect after deleting
