from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

# Import only necessary views
from .views.home import home, list_books, register
from .views.admin_view import admin_view
from .views.librarian_view import librarian_view
from .views.member_view import member_view
from .views.library_detail_view import LibraryDetailView

urlpatterns = [
    path("", home, name="home"),
    path("books/", list_books, name="list_books"),
    path("library/<int:pk>/", LibraryDetailView.as_view(), name="library_detail"),
    path("register/", register, name="register"),
    
    path("login/", LoginView.as_view(template_name="registration/login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="registration/logout.html"), name="logout"),

    # Corrected paths to match the expected view file structure
    path("admin_view/", admin_view, name="admin_view"),
    path("librarian_view/", librarian_view, name="librarian_view"),
    path("member_view/", member_view, name="member_view"),
]
