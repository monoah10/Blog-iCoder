from django.shortcuts import render, HttpResponse
from .models import post

# Create your views here.
def blogHome(request): 
    allPosts= post.objects.all()
    context={'allPosts': allPosts}
    return render(request, "blog/blogHome.html", context)

def blogPost(request, slug): 
    post=post.objects.filter(slug=slug).first()
    context={"post":post}
    return render(request, "blog/blogpost.html", context)