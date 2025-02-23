from django.shortcuts import render, redirect
from django.contrib.auth import login, logout  
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic.detail import DetailView
from django.contrib.auth.views import LoginView, LogoutView
from .models import Library, Book  
from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

def home(request):
    return redirect("relationship_app/list_books")

def list_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  
            return redirect("admin_view")  
    else:
        form = UserCreationForm()
    
    print("Form being sent to template:", form)  # Debugging step
    return render(request, "relationship_app/register.html", {"form": form})

class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")  # Redirect to login after signup
    template_name = "relationship_app/register.html"

class UserLoginView(LoginView):
    template_name = "relationship_app/login.html"

    
class UserLogoutView(LogoutView):
    template_name = "relationship_app//logout.html"

def is_admin(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

def is_librarian(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def is_member(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

@user_passes_test(is_admin)
def admin_view(request):
    return render(request, "relationship_app/admin_dashboard.html")

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, "relationship_app/librarian_dashboard.html")

@user_passes_test(is_member)
def member_view(request):
    return render(request, "relationship_app/member_dashboard.html")