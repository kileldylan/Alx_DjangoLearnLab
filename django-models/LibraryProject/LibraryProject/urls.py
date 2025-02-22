from django.contrib import admin
from django.urls import path
from relationship_app.views import home,list_books, LibraryDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", home, name="home"),  # Home route

    # Function-based view (FBV)
    path('books/', list_books, name='list_books'),

    # Class-based view (CBV) requires `as_view()`
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]
