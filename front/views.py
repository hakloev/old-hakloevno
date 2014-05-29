from django.shortcuts import render
from blog.models import Blogpost
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse

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

def login_view(request):
    return render(request, u'login.html', None)

def login_user(request):
    context = {}
    context['request'] = request
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            context['user'] = user
            return HttpResponseRedirect('/')
        else:
            # Inactive account
            return render(request, u'index.html', context)
    else:
        # Bad login
        return render(request, u'index.html', context)

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')
