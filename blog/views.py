from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'Toshe',
        'title': 'Blog post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'Sashka',
        'title': 'Blog post 2',
        'content': 'Second post content',
        'date_posted': 'August 28, 2019'
    },
]


# Create your views here.
def home(request):
    context = {
        'posts': posts,
        'title': 'Blog Home'
    }
    return render(request, 'blog/home.html', context=context)


def about(request):
    return HttpResponse("<h1> Blog About </h1>")