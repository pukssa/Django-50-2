from django.shortcuts import render, HttpResponse
import random
from .forms import PostCreateForm
import posts
from posts.models import Post
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required


def test_view(request):
    return HttpResponse(f"twinkling watermelon {random.randint(1, 100)}")

def html_view(request):
    return render(request,"main.html")
@login_required(login_url="/login/")
def post_list_view(request):
    post = (Post.objects.all())
    print(posts)
    return render(request,"posts/post_list.html",{"posts":post})
@login_required(login_url="/login/")
def post_detail_view(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request,"posts/post_detail.html", {"posts":post})
@login_required(login_url="/login/")
def create_post_view(request):
    if request.method == "GET":
        form = PostCreateForm(request.POST)
        return render(request,"posts/create_post.html",{"form":form})
    elif request.method == "POST":
        form = PostCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect ('/posts/')
        else:
            return render(request,"posts/create_post.html",{"form":form})