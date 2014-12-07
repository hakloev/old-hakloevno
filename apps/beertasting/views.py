# -*- coding: utf8 -*-

from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from models import Beer, BeerRating, TastingEvent
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.db.models import Avg, Count, Q

import datetime

def index(request):
    latestevents = TastingEvent.objects.filter(finished=False).order_by('-id')
    doneevents = TastingEvent.objects.filter(finished=True).order_by('-id')[:5]
    breadcrumbs = (
            ('Events', reverse('tasting:index')),
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
            ('Events', reverse('tasting:index')),
            (event.name, reverse('tasting:event_by_id', args=[event.id])),
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
        try: 
            r = BeerRating.objects.get(user_id=request.user.id, event_id=eid, beer_id=bid)
            r.rating = request.POST['ratingvalue']
            r.rated = datetime.datetime.now()
            r.save()
            messages.success(request, u'Your rating for beer %s was updated!' % (code))
        except:
            new_r = BeerRating(user=request.user, beer_id=bid, event_id=eid, rating=request.POST['ratingvalue'], comment=request.POST['comment'] )
            new_r.save()
            messages.success(request, u'Your rating for beer %s was registered!' % (code))
        return HttpResponseRedirect(request.path)
    rating = None    
    try:
        rating = BeerRating.objects.get(event=eid, beer_id=bid, user=request.user.id)
    except:
        print 'beer_rating: query not exist'
    comments = BeerRating.objects.filter(event=eid, beer_id=bid).exclude(user__in=[request.user.id])
    beer = Beer.objects.get(id=bid)
    if event.finished:     
        breadcrumbs = (
                ('Events', reverse('tasting:index')),
                (event.name, reverse('tasting:event_by_id', args=[event.id])),
                (u'%s' % (Beer.objects.get(id=bid)), reverse('tasting:beer_rating', args=[event.id, code])),
        )
    else:
        breadcrumbs = (
                ('Events', reverse('tasting:index')),
                (event.name, reverse('tasting:event_by_id', args=[event.id])),
                (u'Beer: %s' % (code), reverse('tasting:beer_rating', args=[event.id, code])),
        )

    return render(request, u'beertasting/ratebeer.html', {
        'request': request,
        'event': event,
        'beer': beer,
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
        ratings = BeerRating.objects.filter(event=event).values('beer').annotate(score=Avg('rating')).order_by('-score')
    else:
        return HttpResponseRedirect('/beertasting/')

    breadcrumbs = (
            ('Events', reverse('tasting:index')),
            (event.name, reverse('tasting:event_by_id', args=[eid])),
            ('Results', reverse('tasting:event_stats', args=[eid])), #Do not need this...
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
    if not request.user.is_staff:
        return render(request, u'denied.html', None)
    beers = Beer.objects.filter(id__in=TastingEvent.objects.get(id=eid).beers.all()).order_by('id')
    event = TastingEvent.objects.get(id=eid)
    ratings = BeerRating.objects.filter(event=event).values('beer').annotate(total=Count('beer')) 
    breadcrumbs = (
            ('Events', reverse('tasting:index')),
            (event.name, reverse('tasting:event_by_id', args=[eid])),
            ('Overview', reverse('tasting:event_list', args=[eid])), #Do not need this...
    )

    return render(request, u'beertasting/adminlist.html', {
        'request': request,
        'beers': beers,
        'ratings': ratings,
        'event':event,
        'breadcrumbs': breadcrumbs}
    )

def beer_stats(request, id): 
    stats = BeerRating.objects.filter(beer_id=id, event_id=TastingEvent.objects.filter(finished=True)).annotate(score=Avg('rating')).order_by('-score')
    beerinfo = BeerRating.objects.filter(beer_id=id, event_id=TastingEvent.objects.filter(finished=True)).values('beer', 'beer__name', 'beer__brewery__name').annotate(score=Avg('rating'), rates=Count('rating'), events=Count('event', distinct=True))
 
    beer = Beer.objects.get(id=id) 
    breadcrumbs = (
            ('Events', reverse('tasting:index')),
            ('Statistics', reverse('tasting:beer_list')),
        (u'%s' % (beer.__unicode__()), None)
    )

    return render(request, u'beertasting/beerstats.html', {
        'request': request,
        'stats': stats,
        'beer': beer,
        'beerinfo': beerinfo,
        'breadcrumbs': breadcrumbs}
    )

def beer_list(request):
    beers = BeerRating.objects.filter(event_id=TastingEvent.objects.filter(finished=True)).values('beer', 'beer__name', 'beer__brewery__name').annotate(score=Avg('rating'), rates=Count('rating'), events=Count('event', distinct=True))

    breadcrumbs = (
            ('Events', reverse('tasting:index')),
            (u'Statistics', reverse('tasting:beer_list'))
    )
    
    return render(request, u'beertasting/beerlist.html', {
            'request': request,
            'breadcrumbs': breadcrumbs,
            'beers': beers}
    )

def beer_overall(request):
    ratings = BeerRating.objects.filter(event_id=TastingEvent.objects.filter(finished=True)).values('beer', 'beer__name', 'beer__brewery__name').annotate(score=Avg('rating'), rates=Count('rating'), events=Count('event', distinct=True)).order_by('-score')[:10] 

    breadcrumbs = (
            ('Events', reverse('tasting:index')),
            ('Top 10', reverse('tasting:beer_overall'))
    )

    return render(request, u'beertasting/beeroverall.html', {
        'request': request,
        'ratings': ratings,
        'breadcrumbs': breadcrumbs}
    )

@login_required
def user_ratings(request,id):
    if not request.user.id == int(id):
        return render(request, u'denied.html', None)
    
    ratings = BeerRating.objects.filter(event_id=TastingEvent.objects.filter(finished=True), user_id=id).order_by('event')
    
    breadcrumbs = (
            ('Events', reverse('tasting:index')),
            ('Statistics', reverse('tasting:beer_list')),
        ('%s' % (request.user.username), None)
    )
    
    return render(request, u'beertasting/userratings.html', {
        'request':request,
        'breadcrumbs': breadcrumbs,
        'ratings': ratings}
    )
