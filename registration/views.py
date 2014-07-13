from django.shortcuts import render

# Create your views here.

def register(request):
    if request.method == 'POST':
        return render(request, u'denied.html', None)
    else:
        return render(request, u'denied.html', None)

def register_success(request):
    return render(request, u'index.html', None)
