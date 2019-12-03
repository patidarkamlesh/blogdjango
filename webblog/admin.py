from django.contrib import admin

from .models import Author, Blog

# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name']


admin.site.register(Author, AuthorAdmin)


class BlogAdmin(admin.ModelAdmin):
    list_display = ['blog_title', 'pub_date', 'author']

admin.site.register(Blog, BlogAdmin)

