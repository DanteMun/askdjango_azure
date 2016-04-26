from django.shortcuts import render, redirect
from .models import Post

from .forms import PostForm
from django.http import HttpResponse
from django.core.urlresolvers import reverse
# Create your views here.



def index(request):
    post_list=Post.objects.all()
    return render(request, 'blog/index.html', {
        'post_list' : post_list,
        })


def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'blog/post_detail.html', {
        'post' : post,
    })

def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            #return redirect('/')
            #방법 1)
            #url = reverse('blog:post_detail', args=[post.pk])
            #return redirect(url)
            #방법 2)
            #return redirect(post.get_absolute_url())
            #방법 3)
            return redirect(post)
    else:
        form = PostForm()
    return render(request, 'blog/post_form.html', {
        'form':form,
        })