from django.shortcuts import render
from models import BeerRating, TastingEvent
from django.http import HttpResponseRedirect
import datetime

# Create your views here.

def index(request):
    context = {}
    context['request'] = request
    try:
        latestevents = TastingEvent.objects.filter(finished=False).order_by('id')
        context['latestevents'] = latestevents
        events = TastingEvent.objects.filter(finished=True).order_by('-id')
        context['events'] = events
    except:
        pass
    return render(request, u'beertasting/index.html', context)

def event_by_id(request, id):
    context = {}
    context['request'] = request
    event = TastingEvent.objects.get(id=id)
    context['event'] = event
    context['beers'] = event.beers
    return render(request, u'beertasting/event.html', context)

def beer_rating(request, eid, bid):
    context = {}
    context['request'] = request
    # ta imot post request, parse og putt i db 
    if request.method == 'POST':
        return HttpResponseRedirect(request.path)
    event = TastingEvent.objects.get(id=eid)
    context['event'] = event
    try: 
        rating = BeerRating.objects.get(event=eid, beer=bid, user=request.user.id)
        context['rating'] = rating
    except:
        pass
     
    return render(request, u'beertasting/ratebeer.html', context)
