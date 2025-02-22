from django.views.generic import DetailView
from ..models import Library  

class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationshup_app/library_detail.html"  
    context_object_name = "library"
