from django.shortcuts import render, redirect
from django.contrib.auth import login, logout  
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView
from django.contrib.auth.views import LoginView, LogoutView
from .models import Library, Book  

def home(request):
    return redirect("list_books")

def list_books(request):
    books = Book.objects.all()
    return render(request, "list_books.html", {"books": books})

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  #
            return redirect("home")  # ✅ Redirect to home after signup
    else:
        form = UserCreationForm()
    return render(request, "register.html", {"form": form})

class LibraryDetailView(DetailView):
    model = Library
    template_name = "library_detail.html"
    context_object_name = "library"

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")  # Redirect to login after signup
    template_name = "register.html"

class UserLoginView(LoginView):
    template_name = "login.html"

class UserLogoutView(LogoutView):
    template_name = "logout.html"
