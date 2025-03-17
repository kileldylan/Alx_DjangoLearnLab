from django.contrib import admin
from .models import Post

# Register your models here.
# Register the Profile Model
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')
