from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views  # Import Django authentication views
from relationship_app.views import home, list_books, LibraryDetailView, SignUpView

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Home route
    path("", home, name="home"),  
    
    # Function-based view (FBV)
    path('books/', list_books, name='list_books'),

    # Class-based view (CBV)
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    
    # User authentication views
    path("register/", SignUpView.as_view(), name="register"),
    path("login/", auth_views.LoginView.as_view(template_name="registration/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),

    # Include Django authentication URLs (for password reset, etc.)
    path("accounts/", include("django.contrib.auth.urls")),
]
