from django.shortcuts import render
from blog.models import Blogpost

# Create your views here.

def index(request):
    context = {}
    context['request'] = request
    try:
        post = Blogpost.objects.latest('posted')
    except:
        post = []
    context['post'] = post
    return render(request, u'index.html', context)
