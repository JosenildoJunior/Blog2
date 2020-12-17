from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required


# Create your views here.

from .models import Post
from .forms import PostForm

def index(request):
    return render(request, 'forum/index.html')


def post(request):
    posts = Post.objects.all()
    contexto = {'posts': posts}
    return render(request, 'forum/post.html', contexto)  

@login_required
def novo_post(request):
    if request.method != 'POST':
        form = PostForm
    else:
        form = PostForm(request.POST)
        if form.is_valid():
            novo_post = form.save(commit=False)
            novo_post.autor = request.user
            novo_post.save()
            return HttpResponseRedirect(reverse('forums:post'))
    contexto = {'form': form}
    return render(request,'forum/novo_post.html', contexto)

@login_required
def edit_post(request, edit_id):
    post = Post.objects.get(id=edit_id)
    if post.autor != request.user:
        raise Http404

    if request.method != 'POST':
        form = PostForm(instance=post)
    else:
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('forums:post'))

    contexto = {'post': post, 'form': form}
    return render(request, 'forum/edit_post.html', contexto)