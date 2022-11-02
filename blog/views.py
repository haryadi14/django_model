from django.shortcuts import render

from .models import Post


def index(request):
    data = Post.objects.all()
    ctx = {
        'title': 'Blog',
        'heading': 'Blog',
        'subheading': 'Postingan',
        'post': data
    }
    return render(request=request, template_name='blog/index.html', context=ctx)