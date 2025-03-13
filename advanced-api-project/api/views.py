from rest_framework import generics, permissions
from  .models import Book
from .serializers import BookSerializer

#view to list(get) and create(post) books
class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly] #Read for all, write for authenticated users

#view to update books
# DetailView: Handles GET (retrieve)
# UpdateView: Handles PUT (update)
# DeleteView: Handles DELETE
class BookDetailUpdateUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly] #restricts updates and deletes