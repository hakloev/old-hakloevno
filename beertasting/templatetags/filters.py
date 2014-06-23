from django import template
import random

register = template.Library()

@register.filter(name='print_select_form')
def print_select_form(rating):
    try:
        int(rating)
    except:
        rating = 1
    string = ""
    for x in range(1,11):
        if x == rating:
            string += '<option value="%s" selected>%s</option>' % (x, x)
        else:
            string += '<option value="%s">%s</option>' % (x, x)

    return string

@register.filter(name='print_beer_info')
def print_beer_info(beers, id):
    string = ""
    for beer in beers:
        if beer.id == id:
            string += '<td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td>' % (beer.name, beer.brewery, beer.style, beer.abv, beer.ibu)
    return string

@register.filter(name='get_number_of_ratings')
def get_number_of_ratings(ratings, id):
    for rating in ratings:
        if rating['beer'] == id:
            return rating['total']
    return 'Ingen'

@register.filter(name='print_rating_icon')
def print_rating_icon(ratings, id):
    for rating in ratings:
        if rating.beer.id == id:
            return '<span class="glyphicon glyphicon-ok"></span>'
    return '<span class="glyphicon glyphicon-remove"></span>'

@register.filter(name='shuffle_beers')
def shuffle_beers(arg):
    beers = list(arg[:])
    random.shuffle(beers)
    return beers

@register.filter(name='get_percent')
def get_percent(number):
    return int(number * 10)

@register.filter(name='get_how_long')
def get_how_long(number, total):
    if number == 0 or total == 0:
        return 0
    return int(((float(number) / float(total)) * 100))
