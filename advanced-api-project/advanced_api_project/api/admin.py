from django.contrib import admin
from .models import Books, Author

# Register your models here.
@admin.register(Books)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title",)
    search_fields = ("title",)

# Author Admin
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)