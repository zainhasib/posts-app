from django.shortcuts import render
from django.http import HttpResponse
import numpy as np

from .models import Posts

# Create your views here.
def index(request):

    posts = Posts.objects.all()[:10]

    context = {
        'title': "Posts",
        'posts': posts
    }

    return render(request, 'posts/index.html', context)

def details(request, id):

    post = Posts.objects.get(id=id)
    arr = np.array(["Zain","Saloni"])
    context = {
        'post': post,
        'arr': arr
    }

    return render(request, 'posts/details.html', context)