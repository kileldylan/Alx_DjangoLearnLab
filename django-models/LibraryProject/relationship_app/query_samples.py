from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author (assuming an author exists)
author = Author.objects.first()  # Fetch the first author
if author:
    books_by_author = author.book_set.all()  # Reverse ForeignKey lookup
    print(f"Books by {author.name}: {books_by_author}")

# List all books in a specific library
library = Library.objects.first()  # Fetch the first library
if library:
    books_in_library = library.books.all()  # ManyToManyField relation
    print(f"Books in {library.name}: {books_in_library}")

# Retrieve the librarian for a library
if library:
    librarian = library.librarian  # Assuming a OneToOneField relation
    print(f"Librarian for {library.name}: {librarian}")
