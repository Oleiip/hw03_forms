from itertools import count
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import Post, Group, User

POSTS_PER_PAGE = 10


def index(request):
    posts = Post.objects.select_related('author',
                                        'group').all()
    paginator = Paginator(posts, POSTS_PER_PAGE)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.groups.all()[:POSTS_PER_PAGE]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)


def profile(request, username):
    posts = Post.objects.filter(author__username=username).all()
    user = User.objects.filter(username=username).values()
    paginator = Paginator(posts, POSTS_PER_PAGE)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'user': user,
        'count': posts.count(),
        'page_obj': page_obj,
    }
    return render(request, 'posts/profile.html', context)


def post_detail(request, post_id):
    post = Post.objects.filter(pk=post_id)
    context = {
        'post': post,
    }
    return render(request, 'posts/post_detail.html', context)


def post_create(request):
    form = {
        'text': text,
        'group': group,
    }
    return render(request, 'posts/create_post.html', form)