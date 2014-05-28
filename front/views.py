from django.shortcuts import render
from blog.models import Blogpost

# Create your views here.

def index(request):
    context = {}
    context['posts'] = Blogpost.objects.all()
    return render(request, u'index.html', context)
