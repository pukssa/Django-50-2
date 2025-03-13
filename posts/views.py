from django.shortcuts import render
from django.http import HttpResponse
from random import randint

def test_view(request):
    return HttpResponse(f"Hello, world.{randint(1, 100)}")

def html_view(request):
    return render(request, "posts/test.html")

# Create your views here.
