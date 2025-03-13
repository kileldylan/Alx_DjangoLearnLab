from django.urls import path
from .views import BookListCreateView, BookDetailUpdateDeleteView

urlpatterns = [
    path('books/', BookListCreateView.as_view(), name='book-list-create'),
    path('books/<int:pk>/', BookDetailUpdateDeleteView.as_view(), name='book-detail-update-delete'),
]
