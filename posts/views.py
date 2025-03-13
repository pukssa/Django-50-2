from django.shortcuts import render
from django.http import HttpResponse
from random import randint

from posts.models import Post


def test_view(request):
    return HttpResponse(f"Hello, world.{randint(1, 100)}")

def home_page_view(request):
    return render(request, "base.html")

def post_list_view(request):
    posts = Post.objects.all()
    return render(request, "post_list.html", context={"posts": posts})

# Create your views here.
