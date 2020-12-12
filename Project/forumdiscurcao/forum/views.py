from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

from .models import Post
from .forms import PostForm

def index(request):
    return render(request, 'forum/index.html')


def post(request):
    posts = Post.objects.all()
    contexto = {'posts': posts}
    return render(request, 'forum/post.html', contexto)  

def novo_post(request):
    if request.method != 'POST':
        form = PostForm
    else:
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('forum:post'))
    contexto = {'form': form}
    return render(request,'forum/novo_post.html', contexto)


    