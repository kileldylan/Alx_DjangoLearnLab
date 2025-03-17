from django.shortcuts import redirect, render
from .forms import CustomUserCreateForm
from django.contrib.auth import login,logout

#view to handle user registration and login
def register(request):
    if request.method == 'POST':
        form = CustomUserCreateForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) #login a user after succesfull login
            return redirect('home')
    else:
        form = CustomUserCreateForm()
    return render(request, 'blog/register.html', {'form': form})

#view for profile management
def profile(request):
    if request.method == 'POST':
        user = request.user
        user.username = request.POST.get('username')
        user.email = request.POST.get('email')
        user.save()
        return redirect('profile')
    else:
        return render(request, 'blog/profile.html', {'user': request.user})

#custom logout view
def custom_logout(request):
    logout(request)
    return redirect('login')