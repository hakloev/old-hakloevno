from django.shortcuts import render
from models import BeerRating, TastingEvent
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
    if event.finished:
        ratings = BeerRating.objects.filter(event=id)
        context['ratings'] = ratings
    if not event.finished:
        context['beers'] = event.beers
    return render(request, u'beertasting/event.html', context)

def rating_by_id(request, eid, rid):
    context = {}
    context['request'] = request
    rating = BeerRating.objects.get(event_id=eid, id=rid)
    context['rating'] = rating
    return render(request, u'beertasting/rating.html', context)
