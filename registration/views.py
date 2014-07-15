# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages 
from django.contrib.auth.models import User

# Create your views here.

def register(request):
    if request.user.is_authenticated():
        messages.error(request, u'Du kan ikke være logget inn når du skal registrere en bruker.')
        return HttpResponseRedirect('/')
    else:
        if request.method == 'POST':
            user = User(
                username=request.POST['username'],
                first_name=request.POST['firstname'],
                last_name=request.POST['lastname'],
                email=request.POST['email'],
            )
            #set user active = false when not validated
            pw1, pw2 = request.POST['password1'], request.POST['password2']
            if pw1 == pw2:
                user.set_password(pw1)
            user.save()
            messages.success(request, u'Din bruker %s ble opprettet.' % (user.username))
            return render(request, u'index.html', None)
        else:
            return render(request, u'registration/register.html', None)

def register_success(request):
    return render(request, u'index.html', None)
