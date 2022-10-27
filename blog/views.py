from multiprocessing import context
from django.shortcuts import render

# Create your views here.
from .models import Post

def index(request):
    db = Post.objects.all()
    context = {
        'title' : 'blog',
        'heading' : 'blog',
        'subheading': 'postingan',
        'post': db,
    }
    return render(request, 'blog/index.html',context)
