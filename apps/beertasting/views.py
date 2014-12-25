# -*- coding: utf8 -*-

from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from models import Beer, BeerRating, TastingEvent, Brewery
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.db.models import Avg, Count, Q, Max

import datetime

def index(request):
    ongoing_events = TastingEvent.objects.filter(finished=False).order_by('-id')
    done_events = TastingEvent.objects.filter(finished=True).order_by('-id')[:5]
    beers = Beer.objects.aggregate(Count('id'))['id__count']
    brewers = Brewery.objects.aggregate(Count('id'))['id__count']
    ratings = BeerRating.objects.aggregate(Count('id'))['id__count']
    events = TastingEvent.objects.aggregate(Count('id'))['id__count']
    rated = Beer.objects.get(id=BeerRating.objects.values('beer__id').annotate(num_ratings=Count('beer__id')).latest('num_ratings')['beer__id'])
    liked = Beer.objects.get(id=BeerRating.objects.values('beer__id').annotate(best=Avg('rating')).latest('best')['beer__id'])
    hated = Beer.objects.get(id=BeerRating.objects.values('beer__id').annotate(lowest=Avg('rating')).earliest('lowest')['beer__id'])
    beers_brewery = Beer.objects.values('brewery__id').annotate(num_beers=Count('brewery__id')).latest('num_beers')['num_beers'] 
    beers_brewery = Brewery.objects.filter(id__in=Beer.objects.values('brewery__id').annotate(num_beers=Count('brewery__id')).filter(num_beers__gte=beers_brewery).values('brewery__id'))
    stats = {
        'ongoing': ongoing_events,
        'done': done_events,
        'beers': beers, 
        'breweries': brewers, 
        'ratings': ratings, 
        'events': events, 
        'most_rated': rated, 
        'most_hated': hated, 
        'most_liked': liked, 
        'most_beers_brewery':beers_brewery
    }
    breadcrumbs = (
            (u'Events', reverse('tasting:index')),
    )

    return render(request, u'beertasting/index.html', {
        'request': request, 
        'breadcrumbs': breadcrumbs,
        'stats': stats,
        }
    )

@login_required
def event_by_id(request, id):
    event = TastingEvent.objects.get(id=id)
    ratings = BeerRating.objects.filter(event=id, user_id=request.user.id)

    breadcrumbs = (
            (u'Events', reverse('tasting:index')),
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
                (u'Events', reverse('tasting:index')),
                (event.name, reverse('tasting:event_by_id', args=[event.id])),
                (u'%s' % (Beer.objects.get(id=bid)), reverse('tasting:beer_rating', args=[event.id, code])),
        )
    else:
        breadcrumbs = (
                (u'Events', reverse('tasting:index')),
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
            (u'Events', reverse('tasting:index')),
            (event.name, reverse('tasting:event_by_id', args=[eid])),
            (u'Results', reverse('tasting:event_stats', args=[eid])), #Do not need this...
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
            (u'Overview', reverse('tasting:event_list', args=[eid])), #Do not need this...
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
            (u'Events', reverse('tasting:index')),
            (u'Statistics', reverse('tasting:beer_list')),
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
            (u'Events', reverse('tasting:index')),
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
            (u'Events', reverse('tasting:index')),
            (u'Statistics', reverse('tasting:beer_list')),
            (u'Top 10', reverse('tasting:beer_overall'))
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
            (u'Events', reverse('tasting:index')),
            (u'Statistics', reverse('tasting:beer_list')),
        ('%s' % (request.user.username), None)
    )
    
    return render(request, u'beertasting/userratings.html', {
        'request':request,
        'breadcrumbs': breadcrumbs,
        'ratings': ratings}
    )
