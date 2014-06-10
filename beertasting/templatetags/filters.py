from django import template

register = template.Library()

@register.filter(name='print_select_form')
def print_select_form(rating):
    try:
        int(rating)
    except:
        rating = 1
    string = ""
    for x in range(1,7):
        if x == rating:
            string += '<option value="%s" selected>%s</option>' % (x, x)
        else:
            string += '<option value="%s">%s</option>' % (x, x)

    return string
