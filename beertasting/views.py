# -*- coding: utf8 -*-

from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from models import Beer, BeerRating, TastingEvent
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.db.models import Avg, Count

import datetime

# Create your views here.

def index(request):
    latestevents = TastingEvent.objects.filter(finished=False).order_by('-id')
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

@login_required
def event_by_id(request, id):
    event = TastingEvent.objects.get(id=id)
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

@login_required
def beer_rating(request, eid, code):
    event = TastingEvent.objects.get(id=eid)
    ratings = BeerRating.objects.filter(event=eid, user_id=request.user.id)
    bid = Beer.objects.get(code=code).id
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
        messages.success(request, u'Dine stemme for øl %s ble registrert!' % (code))
        return HttpResponseRedirect(request.path)
    rating, comments = None, None
    try: 
        rating = BeerRating.objects.get(event=eid, beer_id=bid, user=request.user.id)
        comments = BeerRating.objects.filter(event=eid, beer_id=bid).exclude(user=request.user.id)
    except:
        pass
    
    breadcrumbs = (
            ('Arrangementer', '/beertasting/'),
            (event.name, reverse('event_by_id', args=[event.id])),
            (u'Ølkode %s' % (code), reverse('beer_rating', args=[event.id, code])),
    )

    return render(request, u'beertasting/ratebeer.html', {
        'request': request,
        'event': event,
        'beerid': code,
        'rating': rating,
        'ratings': ratings,
        'comments': comments,
        'breadcrumbs': breadcrumbs}
    )

@login_required
def event_stats(request, eid):
    event = TastingEvent.objects.get(id=eid)
    beers, ratings = None, None
    if event.finished: 
        beers = Beer.objects.filter(id__in=TastingEvent.objects.get(id=eid).beers.all()).order_by('id')
        ratings = BeerRating.objects.filter(event=event).values('beer').annotate(score=Avg('rating'))
    breadcrumbs = (
            ('Arrangementer', '/beertasting/'),
            (event.name, reverse('event_by_id', args=[eid])),
            ('Resultater', reverse('event_stats', args=[eid])), #Do not need this...
    )

    return render(request, u'beertasting/stats.html', {
        'request': request,
        'event': event,
        'beers': beers,
        'ratings': ratings,
        'breadcrumbs': breadcrumbs}
    )

@login_required
def event_list(request, eid):
    beers = Beer.objects.filter(id__in=TastingEvent.objects.get(id=eid).beers.all()).order_by('id')
    event = TastingEvent.objects.get(id=eid)
    ratings = BeerRating.objects.filter(event=event).values('beer').annotate(total=Count('beer')) 
    breadcrumbs = (
            ('Arrangementer', '/beertasting/'),
            (event.name, reverse('event_by_id', args=[eid])),
            ('Oversikt', reverse('event_list', args=[eid])), #Do not need this...
    )

    return render(request, u'beertasting/list.html', {
        'request': request,
        'beers': beers,
        'ratings': ratings,
        'event':event,
        'breadcrumbs': breadcrumbs}
    )
