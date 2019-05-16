from django.contrib import admin
from .models import Blog
from .forms import BlogForm


# Register your models here.

class AdminBlog(admin.ModelAdmin):
    form = BlogForm

admin.site.register(Blog)