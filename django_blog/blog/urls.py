from django.contrib.auth import views as auth_views
from django.urls import path
from blog import views

urlpatterns = [
    path('accounts/login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name = 'login'),
    path('accounts/logout/', views.custom_logout, name='logout'),
    path('accounts/register/', views.register, name='register'),
    path('accounts/profile/', views.profile, name='profile'),
    path('posts/', views.BlogListView.as_view(), name = 'post-list'),
    path('posts/<int:pk>/', views.BlogDetailView.as_view(), name = 'post-detail'),
    path('posts/new', views.BlogCreateView.as_view(), name = 'post-create'),
    path('posts/<int:pk>/edit/', views.BlogUpdateView.as_view, name = 'post-edit'),
    path('posts/<int:pk>/delete/', views.BlogDeleteView.as_view(), name = 'post-delete'),
]