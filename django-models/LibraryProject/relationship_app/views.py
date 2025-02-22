from django.shortcuts import render,redirect
from django.shortcuts import render
from django.http import HttpResponse
from .models import Library, Book  # Import the Book model
from django.views.generic.detail import DetailView

# Create your views here.
def home(request):
    return redirect("list_books")

def list_books(request):
    books = Book.objects.all()  # Fetch all books
    book_list = "\n".join([f"{book.title} - {book.author}" for book in books])  # Format book titles and authors
    return render(request, "relationship_app/list_books.html", {"books": books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"  # Template file to display details
    context_object_name = "library"