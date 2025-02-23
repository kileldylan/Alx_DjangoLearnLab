from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from relationship_app.utils import is_librarian

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_dashboard.html')