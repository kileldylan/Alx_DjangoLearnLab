from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView  # ✅ Import auth views
from . import views  # ✅ Import views from the current app

urlpatterns = [
    path("", views.home, name="home"),
    path("books/", views.list_books, name="list_books"),
    path("library/<int:pk>/", views.LibraryDetailView.as_view(), name="library_detail"),

    # ✅ Authentication URLs (ensure these are exactly as expected)
    path("register/", views.SignUpView.as_view(), name="register"),  # ✅ Ensures views.register is referenced correctly
    path("login/", LoginView.as_view(template_name="registration/login.html"), name="login"),  # ✅ Explicit template name
    path("logout/", LogoutView.as_view(template_name="registration/logout.html"), name="logout"),  # ✅ Explicit template name
]
