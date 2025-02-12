# creating a book instance 
from bookshelf.models import Books

book = Books(title="The Pearl", author="John Steinbeck", publication_year=1938 )
book.save()
# Expected Output: The book instance is successfully created and saved to the database.