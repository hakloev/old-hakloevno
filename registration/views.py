# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages 

# Create your views here.

def register(request):
    if request.user.is_authenticated():
        messages.error(request, u'Du kan ikke være logget inn når du skal registrere en bruker.')
        return HttpResponseRedirect('/')
    else:
        if request.method == 'POST':
            return render(request, u'denied.html', None)
        else:
            return render(request, u'denied.html', None)

def register_success(request):
    return render(request, u'index.html', None)
