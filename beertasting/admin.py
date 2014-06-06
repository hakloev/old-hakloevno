from django.contrib import admin
from models import Beer, Style, BeerRating, Brewery

# Register your models here.
admin.site.register(Beer)
admin.site.register(Style)
admin.site.register(BeerRating)
admin.site.register(Brewery)
