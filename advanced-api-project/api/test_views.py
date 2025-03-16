from django.test import APITestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Book, Author

class BookAPITests(APITestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username="deelan", password="1609@Kilel")
        
        # Initialize the Django test client
        self.client = Client()
        
        # Log in the user (if your views require authentication)
        self.client.login(username="deelan", password="1609@Kilel")
        
        # Create the authors in the test database
        self.author1 = Author.objects.create(name="deelan")  # Create the first author
        self.author2 = Author.objects.create(name="chepchumba winny")  # Create the second author
        
        # Create test books
        self.book1 = Book.objects.create(
            title="Kiki",
            publication_year=2014,
            author=self.author1  # Assign the first author
        )
        self.book2 = Book.objects.create(
            title="Hello World",
            publication_year=2020,
            author=self.author2  # Assign the second author
        )

    # Test Create Book
    def test_create_book(self):
        url = reverse('book-create')  # Ensure this URL name matches your URL configuration
        data = {
            'title': 'New Book',
            'publication_year': 2024,
            'author': self.author1.id,  # Use the first author's ID
        }
        response = self.client.post(url, data, follow=True)
        self.assertEqual(response.status_code, 200)  # Check if the request was successful
        self.assertEqual(Book.objects.count(), 3)  # Check if the book was created

    # Test Retrieve Book
    def test_retrieve_book(self):
        url = reverse('book-detail', args=[self.book1.id])  # Retrieve the first book
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)  # Check if the request was successful
        self.assertContains(response, 'Kiki')  # Check if the correct book is retrieved

    # Test Update Book
    def test_update_book(self):
        url = reverse('book-update', args=[self.book1.id])  # Update the first book
        data = {
            'title': 'Updated Book',
            'publication_year': 2025,
            'author': self.author2.id,  # Use the second author's ID
        }
        response = self.client.post(url, data, follow=True)
        self.assertEqual(response.status_code, 200)  # Check if the request was successful
        self.assertContains(response, 'Updated Book')  # Check if the book is updated

    # Test Delete Book
    def test_delete_book(self):
        url = reverse('book-delete', args=[self.book1.id])  # Delete the first book
        response = self.client.post(url, follow=True)
        self.assertEqual(response.status_code, 200)  # Check if the request was successful
        self.assertEqual(Book.objects.count(), 1)  # Check if the book was deleted

    # Test Filtering
    def test_filter_books(self):
        url = reverse('book-list')
        response = self.client.get(url, {'author': self.author1.id})  # Filter by the first author's ID
        self.assertEqual(response.status_code, 200)  # Check if the request was successful
        self.assertContains(response, 'Kiki')  # Check if the correct book is filtered

    # Test Searching
    def test_search_books(self):
        url = reverse('book-list')
        response = self.client.get(url, {'search': 'Kiki'})  # Search for 'Kiki'
        self.assertEqual(response.status_code, 200)  # Check if the request was successful
        self.assertContains(response, 'Kiki')  # Check if the correct book is found

    # Test Ordering
    def test_order_books(self):
        url = reverse('book-list')
        response = self.client.get(url, {'ordering': 'publication_year'})  # Order by publication year
        self.assertEqual(response.status_code, 200)  # Check if the request was successful
        self.assertContains(response, 'Kiki')  # Check if the books are ordered correctly
        self.assertContains(response, 'Hello World')