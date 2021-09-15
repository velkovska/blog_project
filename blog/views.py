from django.shortcuts import render
from .models import Post

# Create your views here.
def home(request):

    context = {
        'posts': Post.objects.all(),
        'title': 'Blog Home'
    }
    return render(request, 'blog/home.html', context=context)


def about(request):
    context = {
        'title': 'Blog About'
    }
    return render(request, 'blog/about.html', context=context)