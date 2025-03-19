from django.shortcuts import redirect, render
from .forms import CustomUserCreateForm
from django.contrib.auth import login,logout
from django.views.generic import ListView, UpdateView, CreateView, DeleteView, DetailView
from .models import Post
from django.http import HttpResponseForbidden
from .forms import PostForm
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib.auth.decorators import login_required

#view to handle user registration and login
def register(request):
    if request.method == 'POST':
        form = CustomUserCreateForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) #login a user after succesfull login
            return redirect('post-list')
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

class BlogListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'books'

class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

def is_admin(user):
    return user.is_staff

@login_required
class BlogCreateView(UserPassesTestMixin, CreateView):
    model = Post
    template_name = 'blog/post_create_edit.html'
    context_object_name = 'post-create'
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user  # Set logged-in user as author
        return super().form_valid(form)

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden("You must be logged in to perform this action.")
        if not request.user.is_superuser:  # or any other role condition
            return HttpResponseForbidden("You do not have permission to perform this operation!")
        return super().dispatch(request, *args, **kwargs)
    
@login_required
class BlogUpdateView(UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'blog/post_create_edit.html'
    fields = ['title', 'content']

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden("You don't have permissions to Update!")
        return super().dispatch(request, *args, **kwargs)
    
@login_required
class BlogDeleteView(UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    fields = ['title', 'content']
    success_url = '/post/'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden("You don't have permission to Delete")
        return super().dispatch(request, *args, **kwargs)

