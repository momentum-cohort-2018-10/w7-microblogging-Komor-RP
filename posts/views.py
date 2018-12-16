from django.shortcuts import render
from posts.forms import PostForm
from django.views.generic import ListView
from posts.models import Post


class PostListView(ListView):
    model = Post

    def get_queryset(self):
        pass


def index(request):
    form = PostForm()
    return render(request, 'index.html', {
        'form': form
    })
