from django.shortcuts import render
from blog.models import Blogpost

# Create your views here.

def index(request):
    context = {}
    context['request'] = request
    try:
        posts = Blogpost.objects.order_by('-posted')[:3]
    except:
        posts = []
    context['posts'] = posts
    return render(request, u'index.html', context)
