from django.contrib import admin
from posts.models import Post
from posts.models import Category
from posts.models import Tag


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'category', 'rate',)
    list_editable = ('rate',)
    list_display_links = ('title', 'created_at', 'category',)
    list_filter = ('created_at', 'category',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')
    list_display_links = ('name',)



@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')
    list_display_links = ('name',)



