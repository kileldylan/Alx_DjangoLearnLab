# markdown to show how to update the books in the database

from bookshelf.models import Books

retrieved_book = Books.objects.get(title="The Pearl")

#updating the title
retrieved_book.title = "Origin 001"
retrieved_book.save()
# Expected output: Title of the book is succesfully updated and saved to the database