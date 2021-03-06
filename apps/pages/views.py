import requests
from django.shortcuts import render
from apps.blog.models import Blogpost
from django.http import JsonResponse, Http404

# Create your views here.

def index(request):
    context = {}
    context['request'] = request
    try:
        posts = Blogpost.objects.all().order_by('-posted')[:3]
    except:
        posts = []
    context['posts'] = posts
    return render(request, u'pages/index.html', context)

def cv_view(request):
    return render(request, u'pages/cv.html', {})

def bus_times(request):
    if request.method == "GET":
        apiUrl = "http://bybussen.api.tmn.io/rt/"
        stopBerg = {"til": "16011567", "fra": "16010567"}
        stopIla = {"til": "16011192", "fra": "16010192"}
        r1 = requests.get(apiUrl + stopBerg["til"])
        r2 = requests.get(apiUrl + stopIla["til"])
        if (r1.status_code == requests.codes.ok) and (r2.status_code == requests.codes.ok):
            return JsonResponse({"berg": r1.json(), "ila":r2.json()})
        else:
            return JsonResponse({"error": "no response from bybussen.api.tmn.io"})
    else:
        raise Http404

def bus_stops(request):
    apiUrl = "http://bybussen.api.tmn.io/stops/"
    r = requests.get(apiUrl)
    if (r.status_code == requests.codes.ok):
        return JsonResponse(r.json(), safe=False)
    else:
        return JsonResponse({"error": "no response from bybussen.api.tmn.io"})
