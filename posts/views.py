from itertools import imap
from urlparse import urlparse

from django.shortcuts import render

from .models import Post


def index(request):
    def enrich_post(post):
        post.domain = urlparse(post.url).netloc
        return post

    posts = Post.objects.all()
    posts = imap(
        enrich_post,
        posts
    )
    context = {
        'posts': posts
    }
    return render(request, 'index.html', context=context)
