from django.shortcuts import render
from models import BeerRating, TastingEvent
import datetime

# Create your views here.

def index(request):
    context = {}
    context['request'] = request
    events = TastingEvent.objects.all()
    context['events'] = events
    return render(request, u'beertasting/index.html', context)

def event_by_id(request, id):
    context = {}
    context['request'] = request
    ratings = BeerRating.objects.filter(event=id)
    context['ratings'] = ratings
    return render(request, u'beertasting/event.html', context)

def rating_by_id(request, eid, rid):
    context = {}
    context['request'] = request
    rating = BeerRating.objects.get(event_id=eid, id=rid)
    context['rating'] = rating
    return render(request, u'beertasting/rating.html', context)
