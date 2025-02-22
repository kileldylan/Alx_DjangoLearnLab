from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView  # ✅ Import built-in auth views
from . import views  # ✅ Import views from the app

urlpatterns = [
    path("", views.home, name="home"),
    path("books/", views.list_books, name="list_books"),
    path("library/<int:pk>/", views.LibraryDetailView.as_view(), name="library_detail"),

    # ✅ Authentication URLs
    path("register/", views.SignUpView.as_view(), name="register"),
    path("login/", LoginView.as_view(template_name="registration/login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="registration/logout.html"), name="logout"),
]
