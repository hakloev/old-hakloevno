from django.contrib import admin
from models import Beer, Style, BeerRating, TastingEvent, Brewery

class BeerAdmin(admin.ModelAdmin):
    def get_readonly_fields(self, request, obj=None):
        return ('code',)

# Register your models here.
admin.site.register(Beer, BeerAdmin)
admin.site.register(TastingEvent)
admin.site.register(Style)
admin.site.register(BeerRating)
admin.site.register(Brewery)
