from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
def get_books_by_author(author_name):
    author = Author.objects.get(name=author_name)  # Ensure exact lookup
    return Book.objects.filter(author=author)  # Use explicit filtering

# List all books in a library
def get_books_in_library(library_name):
    library = Library.objects.get(name=library_name)  # Match expected query format
    return library.books.all()  # ManyToManyField relation

# Retrieve the librarian for a library
def get_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)  # Match expected query format
    return library.librarian  # OneToOneField relation

# Sample test run (uncomment if testing in Django shell)
# print(get_books_by_author("J.K. Rowling"))
# print(get_books_in_library("Central Library"))
# print(get_librarian_for_library("Central Library"))
