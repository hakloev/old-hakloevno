from django.shortcuts import render
from apps.blog.models import Blogpost

# Create your views here.

def index(request):
    context = {}
    context['request'] = request
    try:
        posts = Blogpost.objects.all().order_by('-posted')[:3]
    except:
        posts = []
    context['posts'] = posts
    return render(request, u'index.html', context)
