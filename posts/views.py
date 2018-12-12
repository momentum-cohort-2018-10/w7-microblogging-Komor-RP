from django.shortcuts import render
from posts.forms import PostForm


def index(request):
    form = PostForm()
    return render(request, 'index.html', {
        'form': form
    })
