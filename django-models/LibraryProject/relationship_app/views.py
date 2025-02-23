from django.shortcuts import render, redirect
from django.contrib.auth import login, logout  
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import user_passes_test
from .models import Library, Book  

def home(request):
    return redirect("list_books")  # ✅ Fixed redirect issue

def list_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  

            # ✅ Redirect based on user role
            if hasattr(user, "userprofile"):
                if user.userprofile.role == "Admin":
                    return redirect("admin_view")
                elif user.userprofile.role == "Librarian":
                    return redirect("librarian_view")
                elif user.userprofile.role == "Member":
                    return redirect("member_view")
            return redirect("home")  # Default redirect

    else:
        form = UserCreationForm()
    
    return render(request, "relationship_app/register.html", {"form": form})

class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "relationship_app/register.html"

class UserLoginView(LoginView):
    template_name = "relationship_app/login.html"

class UserLogoutView(LogoutView):
    template_name = "relationship_app/logout.html"  
    
# Role checking functions with better error handling
def is_admin(user):
    return user.is_authenticated and getattr(user, "userprofile", None) and user.userprofile.role == "Admin"

def is_librarian(user):
    return user.is_authenticated and getattr(user, "userprofile", None) and user.userprofile.role == "Librarian"

def is_member(user):
    return user.is_authenticated and getattr(user, "userprofile", None) and user.userprofile.role == "Member"

# Role-based views
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, "relationship_app/admin_dashboard.html")

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, "relationship_app/librarian_dashboard.html")

@user_passes_test(is_member)
def member_view(request):
    return render(request, "relationship_app/member_dashboard.html")
