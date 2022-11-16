from ast import Return
from email.mime import image
import re
from turtle import home
from urllib import request
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.views.generic.edit import CreateView

from .models import Post_content, Comment
from .form import PostForm, CommentForm

#show post
def newfeed(request):
    data = {"posts": Post_content.objects.all().order_by('-time_create')}# get all post from database
    return render(request, 'pages/new_feed.html', data)

def posts(request, pk):
    posts = Post_content.objects.filter(pk=pk)
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST, request.FILES, username=request.user, post=posts)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    return render(request, "pages/posts.html", {"posts": posts, "form": form})
    
#creat post
def add_Post(request):
    if request.user.is_authenticated:
        add = PostForm()
        return render(request, "pages/post.html", { "f": add })  # add value for f = add
    else:
        return render(request, "pages/error.html")

#save post
def save_Post(request):
    if request.method == "POST":    # method="POST" in template
        saveP = PostForm(request.POST, request.FILES)    # create a variable that takes the request containing the attached data and image file
        if saveP.is_valid():  # if the request is valid
            saveP.save()  # save request
            return HttpResponseRedirect('/')   # back to home
        else:
            return render(request, 'pages/404.html')
    else:
        return render(request, 'pages/404.html')
# error   
def error(request):
    return render(request, 'pages/error.html')


# create comment

def post_comment(reuquest):
    if request.user.is_authenticated:
        add_comment = PostForm(commit=False)
        return render(request, "pages/post.html", { "f": add_comment }) 
    else:
        return render(request, "pages/error.html")

# save comment
def save_comment(request):
    if request.method == "POST":
        save_comment = PostForm(request.POST, request.FILES)
        if save_comment.is_valid():
            save_comment.save()
            return HttpResponseRedirect('/')
        else:
            return render(request, 'pages/404.html')
    else:
        return render(request, 'pages/404.html')

# display comment
def display_comment(request):
    cmt = {"cmt": Comment.objects.all().order_by("-time_comment")}
    return render(request, 'pages/new_feed.html', cmt)
    