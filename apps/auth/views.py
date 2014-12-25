from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def login_view(request):
    redirect_url = request.REQUEST.get('next', '')
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                messages.success(request, 'You successfully logged in as %s' % (user.username))            
                if redirect_url:
                    return HttpResponseRedirect(redirect_url)
                return HttpResponseRedirect('/') 
            else:
                messages.error(request, 'The username %s is disabled!' % (username))
        else:
            messages.error(request, "The username or password was wrong!")
            #return invalid account
    return render(request, u'auth/login.html', {
        'request': request
    })

def logout_view(request):
    logout(request)
    messages.success(request, 'You successfully logged out!')
    return HttpResponseRedirect('/')
