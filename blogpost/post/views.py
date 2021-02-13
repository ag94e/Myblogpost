from django.shortcuts import render, get_object_or_404
from .models import PostModel

def home (request):

    all_posts = PostModel.objects.all()

    return render(request, 'index.html', {'posts' : all_posts})

def single_post (request, post):

    post_request = get_object_or_404(PostModel, slugname=post)

    return render(request, 'single_post.html', {'post' : post_request})