"""
    Model.objects.all() - Возрващает все записи из базы данных
    Model.objects.get() - Возрващает одну запись из базы данных (с условием)
    Model.objects.filter() - Возрващает записи с условием
"""

from django.shortcuts import render
from posts.models import Post


def post_list_view(request):
    post = Post.objects.all()