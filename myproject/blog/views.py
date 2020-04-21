from django.shortcuts import render
from .models import BlogPost
from django.http import HttpResponse
from django.template import loader

def archive(request):
    posts = BlogPost.objects.all()
    template = loader.get_template('blog/archive.html')
    context = {
        'posts': posts,
    }
    return HttpResponse(template.render(context, request))
