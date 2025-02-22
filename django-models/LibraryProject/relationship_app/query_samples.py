from relationship_app.models import Author, Book, Library, Librarian

def get_books_by_author(author_name):
    """Query all books by a specific author."""
    return Book.objects.filter(author__name=author_name)

def list_books_in_library(library_name):
    """List all books in a specific library."""
    return Book.objects.filter(library__name=library_name)

def get_librarian_for_library(library_name):
    """Retrieve the librarian responsible for a library."""
    try:
        library = Library.objects.get(name=library_name)
        return library.librarian  # Assuming a OneToOne or ForeignKey relationship
    except Library.DoesNotExist:
        return None

if __name__ == "__main__":
    author_name = "J.K. Rowling"
    library_name = "Central Library"

    books_by_author = get_books_by_author(author_name)
    print(f"Books by {author_name}: {[book.title for book in books_by_author]}")

    books_in_library = list_books_in_library(library_name)
    print(f"Books in {library_name}: {[book.title for book in books_in_library]}")

    librarian = get_librarian_for_library(library_name)
    if librarian:
        print(f"Librarian for {library_name}: {librarian.name}")
    else:
        print(f"No librarian found for {library_name}")
