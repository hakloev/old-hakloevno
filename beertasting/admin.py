from django.contrib import admin
from models import Beer, Style, BeerRating, BeerTasting, Brewery

# Register your models here.
admin.site.register(Beer)
admin.site.register(Style)
admin.site.register(BeerRating)
admin.site.register(Brewery)
admin.site.register(BeerTasting)
