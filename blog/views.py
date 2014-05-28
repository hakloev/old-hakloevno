from django.shortcuts import render, get_object_or_404
from blog.models import Blogpost, Category

# Create your views here.

def index(request):
    context = {}
    context['categories'] = Category.objects.all()
    context['posts'] = Blogpost.objects.all()
    return render(request, u'blog/blog.html', context)

def newpost(request):
    context = {}
    return render(request, u'blog/newpost.html', context)

def post_by_slug(request, slug):
    post = get_object_or_404(Blogpost, slug=slug)
    context = {}
    #context['categories'] = Category.objects.all()
    #context['post'] = Blogpost.objects.filter(slug=slug)
    context['post'] = post
    return render(request, u'blog/article.html', context)
