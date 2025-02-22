from django.contrib import admin
from django.urls import path
from relationship_app.views import home, list_books, LibraryDetailView, SignUpView, UserLoginView, UserLogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", home, name="home"),  

    # Function-based view (FBV)
    path('books/', list_books, name="list_books"),

    # Class-based view (CBV) requires `as_view()`
    path('library/<int:pk>/', LibraryDetailView.as_view(), name="library_detail"),
    
    # Authentication URLs
    path("register/", SignUpView.as_view(), name="register"),
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", UserLogoutView.as_view(), name="logout"),
]
