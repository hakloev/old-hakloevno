from django.shortcuts import render
from models import Beer, BeerRating
import datetime

# Create your views here.

def index(request):
    context = {}
    context['request'] = request
    ratedbeers = BeerRating.objects.filter(user_id=request.user.id, rated=datetime.date.today())
    context['ratings'] = ratedbeers
    return render(request, u'beertasting/index.html', context)

