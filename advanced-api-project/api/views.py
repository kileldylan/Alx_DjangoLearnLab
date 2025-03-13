from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Book
from .serializers import BookSerializer

# ListView (Public Read, Authenticated Users Can Create)
class BookListView(ListView):
    model = Book
    template_name = 'book_list.html'
    context_object_name = 'books'

# DetailView (Public Read)
class BookDetailView(DetailView):
    model = Book
    template_name = 'book_detail.html'

# CreateView (Only Authenticated Users)
class BookCreateView(LoginRequiredMixin, CreateView):
    model = Book
    template_name = 'book_create.html'
    fields = ['title', 'author', 'description', 'published_date']
    login_url = '/login/'  # Redirect to login page if unauthenticated

# UpdateView (Only Authenticated Users)
class BookUpdateView(LoginRequiredMixin, UpdateView):
    model = Book
    template_name = 'book_update.html'
    fields = ['title', 'author', 'description', 'published_date']
    login_url = '/login/'

# DeleteView (Only Authenticated Users)
class BookDeleteView(LoginRequiredMixin, DeleteView):
    model = Book
    template_name = 'book_delete.html'
    success_url = '/'  # Redirect after deleting
    login_url = '/login/'
