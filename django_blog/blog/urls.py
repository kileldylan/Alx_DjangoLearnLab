from django.contrib.auth import views as auth_views
from django.urls import path
from blog import views

urlpatterns = [
    path('accounts/login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name = 'login'),
    path('accounts/logout/', views.custom_logout, name='logout'),
    path('accounts/register/', views.register, name='register'),
    path('accounts/profile/', views.profile, name='profile'),
    path('post/', views.PostListView.as_view(), name = 'post-list'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name = 'post-detail'),
    path('post/new/', views.PostCreateView.as_view(), name = 'post-create'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name = 'post-edit'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name = 'post-delete'),
    path('post/<int:pk>/comment/new/', views.CommentCreateView.as_view(), name = 'comment-create'),
    path('post/<int:pk>/comments/', views.CommentListView.as_view(), name = 'comment-list'),
    path('post/<int:pk>/comment/update/', views.CommentUpdateView.as_view(), name='comment-update'),
    path('post/<int:pk>/comment/delete/', views.CommentDeleteView.as_view(), name='comment-delete'),
]