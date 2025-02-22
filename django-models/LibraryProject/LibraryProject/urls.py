from django.contrib import admin
from django.urls import path, include  # ✅ Include is needed for app-level URLs

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("relationship_app.urls")),  # ✅ Include the correct app
]
