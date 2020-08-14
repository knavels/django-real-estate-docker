from django.shortcuts import render
from listings.models import Listing
from realtors.models import Realtor

from random import choice

# Create your views here.
def index(request):
    """index page for pages view"""
    listings = Listing.objects.filter(is_published=True).order_by('-list_date')[:3]

    context = {
        'listings': listings
    }

    return render(request, 'pages/index.html', context)


def about(request):
    """Shows about page"""

    #get all realtors
    realtors = Realtor.objects.order_by('-hire_date')

    #get mvp
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)
    mvp_realtor = []

    if mvp_realtors:
        mvp_realtor = choice(mvp_realtors)

    context = {
        'realtors': realtors,
        'mvp_realtor': mvp_realtor
    }

    return render(request, 'pages/about.html', context)