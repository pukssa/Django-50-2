from unicodedata import category

from django.shortcuts import render, HttpResponse
import random
from .forms import PostCreateForm, SearchForm, PostUpdateForm
import posts
from posts.models import Post
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.views.generic import ListView, DetailView, CreateView




def test_view(request):
    return HttpResponse(f"twinkling watermelon {random.randint(1, 100)}")



def html_view(request):
    return render(request,"main.html")








@login_required(login_url="/login/")
def post_list_view(request):
    form = SearchForm()
    query_params = request.GET
    limit = 3
    if request.method == "GET":

        posts = Post.objects.all()
        category_id = query_params.get("category")
        tags = query_params.get("tags")
        search = query_params.get("search")
        ordering = query_params.get("ordering")
        page = int(query_params.get("page",)) if query_params.get("page") else 1

        if search:
             posts = posts.filter(Q(title__icontains=search) | Q(content__icontains=search)
            )

        if category_id:
            posts = posts.filter(category=category_id)

        if tags:
            tags = [int(tag) for tag in tags]
            posts = posts.filter(tag__in=tags)

        if ordering:
            posts = posts.order_by(ordering)


        max_pages = posts.count() / limit
        if round(max_pages)  < max_pages:
            max_pages = round(max_pages) +1
        else:
            max_pages = round(max_pages)

        start = (page - 1) * limit
        end = (page) * limit
        posts = posts[start:end]
        return render (
            request,
            "posts/post_list.html",
            context={"posts": posts, "form": form, "max_pages": range(1, max_pages + 1)},
        )



class PostListView(ListView):
    model = Post
    template_name = "posts/post_list.html"
    context_object_name = "posts"




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



@login_required(login_url="/login/")
def post_update_view(request, post_id):
    try:
        post = Post.objects.get(id=post_id, author=request.user)
    except Post.DoesNotExist:
        return HttpResponse("Post does not exist")
    if request.method == "GET":
        form = PostUpdateForm(instance=post)
        return render(request,"posts/post_update.html",{"form":form})
    if request.method == "POST":
        form = PostUpdateForm(request.POST, request.FILES ,instance=post)
        if not form.is_valid():
            return render(request,"posts/post_update.html",{"form":form})
        if form.is_valid():
            form.save()
            return redirect ('/profile/')
        else:
             return HttpResponse("Post does not edit")





