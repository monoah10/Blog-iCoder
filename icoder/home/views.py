from django.shortcuts import render,HttpResponse
from .models import Contact
from blog.models import post
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,'home/home.html')

def contact(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        content =request.POST['content']
        if len(name)<2 or len(email)<3 or len(phone)<10 or len(content)<4:
            messages.error(request, "Please fill the form correctly")
        else:
            contact=Contact(name=name, email=email, phone=phone, content=content)
            contact.save()
            messages.success(request, "Your message has been successfully sent")
    return render(request, "home/contact.html")


def about(request):
    return render(request,'home/about.html')
    # return HttpResponse('about')

def search(request):
    query=request.GET['query']
    if len(query)>78:
        allPosts=post.objects.none()
    else:
        allPostsTitle= post.objects.filter(title__icontains=query)
        allPostsAuthor= post.objects.filter(author__icontains=query)
        allPostsContent =post.objects.filter(content__icontains=query)
        allPosts=  allPostsTitle.union(allPostsContent, allPostsAuthor)
    if allPosts.count()==0:
        messages.warning(request, "No search results found. Please refine your query.")
    params={'allPosts': allPosts, 'query': query}
    return render(request, 'home/search.html', params)