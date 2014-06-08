from django.shortcuts import render
from models import BeerRating, TastingEvent
from django.http import HttpResponseRedirect
import datetime

# Create your views here.

def index(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/accounts/login/?next=/beertasting/')
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
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/accounts/login/?next=/beertasting/event%s' % (id))
    context = {}
    context['request'] = request
    event = TastingEvent.objects.get(id=id)
    context['event'] = event
    context['beers'] = event.beers
    return render(request, u'beertasting/event.html', context)

def beer_rating(request, eid, bid):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/accounts/login/?next=/beertasting/event%s/beer%s' % (eid, bid))
    context = {}
    context['request'] = request
    event = TastingEvent.objects.get(id=eid)
    context['event'] = event
    context['beerid'] = bid
    context['beers'] = event.beers

    if request.method == 'POST':
        return HttpResponseRedirect(request.path)
    try: 
        rating = BeerRating.objects.get(event=eid, beer=bid, user=request.user.id)
        context['rating'] = rating
    except:
        pass
    return render(request, u'beertasting/ratebeer.html', context)

def stats(request, eid):
    context = {}
    event = TastingEvent.objects.get(id=eid)
    context['event'] = event
    return render(request, u'beertasting/stats.html', context)
