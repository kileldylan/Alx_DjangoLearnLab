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
            return redirect("home")  
    else:
        form = UserCreationForm()
    return render(request, "register.html", {"form": form})

class LibraryDetailView(DetailView):
    model = Library
    template_name = "library_detail.html"
    context_object_name = "library"

def user_register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
        else: 
            form = UserCreationForm()
            return render(request, "register.html", {"form": form})
'''     
class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")  # Redirect to login after signup
    template_name = "register.html"

    '''
def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")
        else:
            form = AuthenticationForm()
            return render(request, "login.html", {"form": form})

def user_logout(request):
    if request.method == "POST":
        logout(request)
        return redirect("home")
    
'''
class UserLoginView(LoginView):
    template_name = "login.html"

class UserLogoutView(LogoutView):
    template_name = "logout.html"

    '''