from django.shortcuts import redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.models import User
from relationship_app.models import UserProfile  # Import your UserProfile model

class CustomLoginView(LoginView):
    def form_valid(self, form):
        """Override form_valid to check user role after login"""
        user = form.get_user()
        login(self.request, user)  # Log in the user

        # Check if the user has a profile and get their role
        try:
            user_profile = UserProfile.objects.get(user=user)
            if user_profile.role == "admin":
                return redirect("admin_view")
            elif user_profile.role == "librarian":
                return redirect("librarian_view")
            elif user_profile.role == "member":
                return redirect("member_view")
        except UserProfile.DoesNotExist:
            pass  # If no UserProfile exists, fallback to default behavior

        return redirect("home")  # Redirect to home if no role is found
