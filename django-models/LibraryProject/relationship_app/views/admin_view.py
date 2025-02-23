from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from relationship_app.utils import is_admin

@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_dashboard.html')