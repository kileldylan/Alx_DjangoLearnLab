from django.shortcuts import render,redirect
from django.shortcuts import render
from django.http import HttpResponse
from .models import Book, Library  # Import the Book model
from django.views.generic.detail import DetailView

# Create your views here.
def home(request):
    return redirect("list_books")

def list_books(request):
    books = Book.objects.all()  # Fetch all books
    book_list = "\n".join([f"{book.title} - {book.author}" for book in books])  # Format book titles and authors
    return HttpResponse(f"List of Books:\n{book_list}", content_type="text/plain")

class LibraryDetailView(DetailView):
    model = Library
    template_name = "library_detail.html"  # Template file to display details
    context_object_name = "library"