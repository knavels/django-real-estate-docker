from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from . import models


def index(request):
    """Shows list of listings"""
    listings = models.Listing.objects.filter(is_published=True).order_by('-list_date')

    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    page_listings = paginator.get_page(page)

    context = {
        'listings': page_listings
    }
    return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
    """Shows details for specific listings"""
    listing = get_object_or_404(models.Listing, pk=listing_id)

    context = {
        'listing': listing
    }

    return render(request, 'listings/listing.html', context)


def search(request):
    """Searching listings page"""
    return render(request, 'listings/search.html')
