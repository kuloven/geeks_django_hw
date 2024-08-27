from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render
from django.http import HttpResponse
from posts.models import Post
from django.shortcuts import redirect
from posts.forms import PostForm, SearchForm
import random


def word(request):
    if request.method == 'GET':
        return HttpResponse('Hello my friend. You play dota 2?')

def main_page(request):
    if request.method == 'GET':
        return render(request, template_name='main_page.html')

@login_required(login_url='login')
def post_list_view(request):
    if request.method == 'GET':
        search = request.GET.get('search')
        tags = request.GET.getlist('tags')
        orderings = request.GET.get('orderings')
        searchform = SearchForm(request.GET)
        page = int(request.GET.get('page', 1))
        posts = Post.objects.all()
        if search:
            posts = posts.filter(Q(title__icontains=search) | Q(content__icontains=search))
        if tags:
            posts = posts.filter(tags__id__in=tags)
        if orderings:
            posts = posts.order_by(orderings)

        limit = 3
        max_pages = posts.count() / limit
        if round(max_pages)<max_pages:
            max_pages = round(max_pages) + 1
        else:
            max_pages = round(max_pages)
        start = (page-1) * limit
        end = page * limit
        posts = posts[start:end]
        context = {'posts': posts, 'search_form': searchform, 'max_pages': range(1, max_pages+1)}
        return render(request, template_name='posts/post_list.html', context=context)

@login_required(login_url='login')
def post_detail_view(request, post_id):
    if request.method == 'GET':
        post = Post.objects.get(id=post_id)
        return render(request, 'posts/post_detail.html', context={'post': post})

@login_required(login_url='login')
def post_create_view(request):
    if request.method == 'GET':
        form = PostForm()
        return render(request, 'posts/post_create.html', context={'form': form})
    if request.method =='POST':
        # Post.objects.create(
        # image=image,
        # title=title,
        # content=content,
        # rate=rate
        # )
        return redirect('/posts/')