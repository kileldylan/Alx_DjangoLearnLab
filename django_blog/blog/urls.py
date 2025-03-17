from django.contrib.auth import views as auth_views
from django.urls import path
from blog import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view, template_name=('blog/login.html'), name = 'login'),
    path('logout/', views.custom_logout, name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
]