# -*- coding: utf8 -*-

from django.shortcuts import render
from django.contrib import messages
from models import BeerRating, TastingEvent
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
import datetime

# Create your views here.

def index(request):
    latestevents = TastingEvent.objects.filter(finished=False).order_by('id')
    doneevents = TastingEvent.objects.filter(finished=True).order_by('-id')
    
    breadcrumbs = (
        ('Arrangementer', '/beertasting/'),
    )

    return render(request, u'beertasting/index.html', {
        'request': request, 
        'breadcrumbs': breadcrumbs,
        'latestevents': latestevents,
        'doneevents': doneevents}
    )

def event_by_id(request, id):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/') #TODO: fix redirect to unauthorized
    event = TastingEvent.objects.get(id=id)
    # Ratings does only show when event is finished. Check for that in view for optimalization?
    ratings = BeerRating.objects.filter(event=id, user_id=request.user.id)
    
    breadcrumbs = (
            ('Arrangementer', '/beertasting/'),
            (event.name, reverse('event_by_id', args=[event.id])),
    )

    return render(request, u'beertasting/event.html', {
        'request':request,
        'event': event,
        'ratings': ratings,
        'breadcrumbs':breadcrumbs}
    )

def beer_rating(request, eid, bid):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/') #TODO: fix redirect to unauthorized
    event = TastingEvent.objects.get(id=eid)
    
    if request.method == "POST":
        rating = request.POST['ratingvalue']
        comment = request.POST['comment']
        try: 
            r = BeerRating.objects.get(user_id=request.user.id, event_id=eid, beer_id=bid)
            r.rating = rating
            r.comment = comment
            r.rated = datetime.datetime.now()
            r.save()
        except:
            new_r = BeerRating(user=request.user, beer_id=bid, event_id=eid, rating=rating, comment=comment )
            new_r.save()
        messages.success(request, u'Dine stemme for øl %s ble registrert!' % (bid))
        return HttpResponseRedirect(request.path)
    rating = None
    try: 
        rating = BeerRating.objects.get(event=eid, beer=bid, user=request.user.id)
    except:
        pass
    
    breadcrumbs = (
            ('Arrangementer', '/beertasting/'),
            (event.name, reverse('event_by_id', args=[event.id])),
            (u'Øl %s' % (bid), reverse('beer_rating', args=[event.id, bid])),
    )

    return render(request, u'beertasting/ratebeer.html', {
        'request': request,
        'event': event,
        'beerid': bid,
        'rating': rating,
        'breadcrumbs': breadcrumbs}
    )

def stats(request, eid):
    context = {}
    event = TastingEvent.objects.get(id=eid)
    context['event'] = event
    return render(request, u'beertasting/stats.html', context)
