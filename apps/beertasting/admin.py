from django.contrib import admin
from models import Beer, Style, BeerRating, TastingEvent, Brewery

class RatingAdmin(admin.ModelAdmin):
    def get_readonly_fields(self, request, obj=None):
        return ('beer', 'user', 'event', 'rating', 'comment',)

class BeerAdmin(admin.ModelAdmin):
    def get_readonly_fields(self, request, obj=None):
        return ('code',)

# Register your models here.
admin.site.register(Beer, BeerAdmin)
admin.site.register(TastingEvent)
admin.site.register(BeerRating, RatingAdmin)
admin.site.register(Style)
admin.site.register(Brewery)
