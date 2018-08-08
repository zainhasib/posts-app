from django.shortcuts import render
from django.http import HttpResponse

from .models import Images

# Create your views here.
def index(request):


    images = Images.objects.all();

    context = {
        'images': images,
    }

    return render(request, 'gallery/index.html', context)