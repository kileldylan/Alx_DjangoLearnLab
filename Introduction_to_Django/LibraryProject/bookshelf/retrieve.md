# markdown to illustrate retieving a book by title

from bookshelf.models import Books

retrieved_book = Books.objects.get(title="Origin 001")
print(retrieved_book)

# Expected Output: <Books: Books object (1)> (or similar output showing the book instance)