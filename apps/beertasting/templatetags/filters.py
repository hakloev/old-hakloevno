from django import template

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
    return 'None'

@register.filter(name='print_rating_icon')
def print_rating_icon(ratings, id):
    for rating in ratings:
        if rating.beer.id == id:
            return '<i class="fa fa-check"></i>'
    return '<i class="fa fa-close"></i>'

@register.filter(name='shuffle_beers')
def shuffle_beers(arg):
    # Orders beerlist by code, alphabetically. 
    beers = list(arg[:])
    return sorted(beers, key=lambda x: x.code, reverse=False)

@register.filter(name='get_percent')
def get_percent(ratings, number):
    return int((float(ratings) / float(number)) * 100)
   
