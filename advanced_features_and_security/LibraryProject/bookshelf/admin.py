from django.contrib import admin
from bookshelf.models import (
    UserProfile, Author, Book, Library, Librarian
)

# User Profile Admin
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "role", "bio")
    search_fields = ("user__email", "role")

# Author Admin
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)

# Book Admin
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "published_date", "isbn")
    search_fields = ("title", "author", "isbn")

# Library Admin
@admin.register(Library)
class LibraryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)

# Librarian Admin
@admin.register(Librarian)
class LibrarianAdmin(admin.ModelAdmin):
    list_display = ("name", "library")
    search_fields = ("name", "library__name")
