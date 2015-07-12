from django.contrib import admin
from posts.models import Post, Category, Blog


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'summary', 'body', 'url_image', 'published_date')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

class BlogAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Post, PostAdmin),
admin.site.register(Category, CategoryAdmin),
admin.site.register(Blog, BlogAdmin),

