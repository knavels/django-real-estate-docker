from django.shortcuts import render


def index(request):
    """Shows list of listings"""
    return render(request, 'listings/listings.html')


def listing(request):
    """Shows details for specific listings"""
    return render(request, 'listings/listing.html')


def search(request):
    """Searching listings page"""
    return render(request, 'listings/search.html')
