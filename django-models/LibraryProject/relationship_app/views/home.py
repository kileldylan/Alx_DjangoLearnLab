from django.shortcuts import render
from relationship_app.models import Book  # Ensure the correct model is imported

def home(request):
    return render(request, "relationship_app/list_books.html")

def list_books(request):
    books = Book.objects.all()  # Fetch all books from the database
    return render(request, "relationship_app/list_books.html", {"books": books})

def register(request):
    return render(request, "registration/register.html")
