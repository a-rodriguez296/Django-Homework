from django.contrib import admin
from posts.models import Post, Category


class PostAdmin(admin.ModelAdmin):
    list_display = ('owner', 'title', 'summary', 'body', 'url_image', 'published_date')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Post, PostAdmin),
admin.site.register(Category, CategoryAdmin),

